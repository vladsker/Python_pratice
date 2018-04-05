person={}

person={"age":12,"first_name":"Brian","last_name":"Layk","city":"Lisbon"}

print(person["age"])

favourite_numbers={"Anna":12}

#favourite_numbers+{"Annabel":12}


user={
    "username":"efermi",
    "first_name":"Eneriko",
    "last_name":"Fermi"
}

print("\n",user)

for key,value in user.items():
    print("\n","Key is :\t",key,"\n","Value is :\t",value)

user.update({"sd":"sd"})

for key,value in user.items():
    print("\n", "Key is :\t", key, "\n", "Value is :\t", value)
