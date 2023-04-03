while True:
    # Creating a dict to store the workers info in thier IDs
    workers = {
        9012597022: {"name": "Bright", "password": "stdapps1!", "ratings": [5, 2, 6]},
        9012597023: {"name": "David", "password": "stdapps2!", "ratings": [2, 1, 9]},
        9012597024: {"name": "Francis", "password": "stdapps3!", "ratings": []},
        9012597025: {"name": "Oscar", "password": "stdapps4!", "ratings": [2, 1, 9]}
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
            while True:
                password = input("Please enter your password to continue: ")
                if not password == workers[uid]["password"]:
                    print("Incorrect Password! Please Try again.")
                    continue
                else:
                    print("Login Successfully")
                    break

    except ValueError:
        print("Invalid input. Try again!")
        continue
    except:
        print("Invalid input. Try again!")
        continue
