from unittest import TestCase
from unittest.mock import patch
import io

class TestWorkerRatings(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['9012597022', 'stdapps1!', '7', '8', '9', '10', '9012597023', 'stdapps2!', '1', '2', '3', '4', '9012597024', 'stdapps3!', '5', '6', '7', '8', '9012597025', 'stdapps4!', '9', '10', '8', '7', '6', '5'])
    def test_worker_ratings(self):
        # Set up workers and ratings
        limit = 3
        num_ratings_given = [3, 3, 3, 3]  # Update this based on the number of workers
        workers = {
            9012597022: {"name": "Bright", "password": "stdapps1!", "ratings": []},
            9012597023: {"name": "David", "password": "stdapps2!", "ratings": []},
            9012597024: {"name": "Francis", "password": "stdapps3!", "ratings": []},
            9012597025: {"name": "Oscar", "password": "stdapps4!", "ratings": []}
        }

        # Simulate worker logins and ratings
        for uid, worker_info in workers.items():
            # Login
            self.assertEqual(login(uid, worker_info, limit), "success")

            # Rate other workers
            for other_id, other_info in workers.items():
                if uid == other_id:
                    continue  # Don't rate self
                rate_worker(worker_info, other_info)

        # Check that each worker has the correct number of ratings
        for i, worker_info in enumerate(workers.values()):
            expected_num_ratings = num_ratings_given[i]
            actual_num_ratings = len(worker_info["ratings"])
            self.assertEqual(actual_num_ratings, expected_num_ratings)

        # Check that all workers have been rated
        self.assertTrue(all(len(w["ratings"]) == sum(num_ratings_given) - 4 for w in workers.values()))