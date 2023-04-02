workers = {
           9012597022: {"name": "Bright", "password": "stdapps1!", "ratings": [5, 2, 6]},
           9012597023: {"name": "David", "password": "stdapps2!", "ratings": [2, 1, 9]},
           9012597024: {"name": "Francis", "password": "stdapps3!", "ratings": []},
           9012597025: {"name": "Oscar", "password": "stdapps4!", "ratings": [2, 1, 9]}
}
# print(workers[9012597024])
# for i in range(1, 4):#
#     workers[9012597024]["ratings"].append(i)

My_pass = input("Enter password: ")
uid = int(input("Enter Username: "))
print(My_pass == workers[uid]["password"])