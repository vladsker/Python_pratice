username_list = ["vskuba","admin","iuser","iuser2","iuser3"]

for user in username_list:
    if user=="admin":
        print("\nHello, ", user, ", would you like to see a status report?")
    else:
        print("\nHello Eric, thank you for logging in again.")

current_users_list = ["uSer1", "user2", "User3", "user4", "user5"]
new_users_list = ["User1", "User2"]

current_users_list_lower=[]

for i in current_users_list:
    current_users_list_lower.append(i.lower())

for user in new_users_list:
    if current_users_list_lower.count(user.lower())>0:
        print("\nUser exist")
    else:
        print("\nUser not exist")