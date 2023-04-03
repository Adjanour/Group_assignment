limit = 3
num_ratings_given = []
# Creating a dict to store the workers info in thier IDs
workers = {
    9012597022: {"name": "Bright", "password": "stdapps1!", "ratings": []},
    9012597023: {"name": "David", "password": "stdapps2!", "ratings": []},
    9012597024: {"name": "Francis", "password": "stdapps3!", "ratings": []},
    9012597025: {"name": "Oscar", "password": "stdapps4!", "ratings": []}
}
# A worker verifies and acesses thier info by entering thier UID and password.
while True:
    try:
        uid = input("Please enter your UID  (Hint 10-digit number): ")
        uid = int(uid)
        if not uid in workers:
           print("Incorrect UID! Please Try again.")
           continue
        else:
            limit = 3
            while limit >=0:
                password = input("Please enter your password to continue: ")
                correct_logins = password == workers[uid]["password"]
                if not correct_logins:
                    print(f"Incorrect Password! you have {limit} attempts remaining")
                    limit-=1
                    continue
                else:
                    print("")
                    print("Login Successful")
                    print(f"Welcome {workers[uid]['name']}")

                    break
            if limit < 0:
                print("You have exceed the number of limits. I was right about my suspicions. Try again later")
                break
            # Here the loop iterates through the dictionary grouping its items into keys and values.
            for worker_id, worker_info in workers.items():
                if worker_id == uid:
                    continue
                print(f"""
========================================
On a scale of 1 to 10
1-5: Not working lately     6: As Expected   7-10: Hardworking

How would you rate {worker_info['name']}'s performance this month
========================================

""")
                while True:
                    try:
                        rating = int(input(": "))
                        print(worker_info)
                        if not rating in range(1, 11):
                            print("Enter an number between 1 and 10 inclusive")
                            continue
                        worker_info["ratings"].append(rating)
                        print(worker_info)
                        break
                    except ValueError:
                        print("Invalid input *. Please try again.")
                        continue
            all_rated = all(len(w["ratings"]) == len(workers) - 1 for w in workers.values())
            print(all_rated)
            if not all_rated:
                continue
            else:
                print("Everyone has been rated")
                break

    except ValueError:
        print("Invalid input**. Try again!")
        continue
    except:
        print("Invalid input***. Try again!")
        continue

print("Success! Lets make progress")