print("\n\n\n\nHello, dear. Do you want to add user for voting? ")

answer=input("Y/N\n")

users={}

if answer.upper()=="Y":
    name = input("\nPlease, type first name: ")
    surname = input("\nPlease, type surname: ")
    users.update({name:surname})

print("\nMore to add? ")
answer = input("Y/N\n")
if answer.upper() == "Y":
    name = input("\nPlease, type first name: ")
    surname = input("\nPlease, type surname: ")
    users.update({name: surname})

print("\nMore to add? ")
answer = input("Y/N\n")
if answer.upper() == "Y":
    name = input("\nPlease, type first name: ")
    surname = input("\nPlease, type surname: ")
    users.update({name: surname})

pooled_users={"Anna":"Karenina", "Ivan":"Kotov"}

for name,surname in pooled_users.items():
    if name in users.keys():
        if users[name]==surname:
            print("Voilla! " + " user " + name + " " + surname + " exists.")

print(users)