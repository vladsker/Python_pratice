print("\n----------------------------------------------")
print("\nTask1: ")

rivers={}

rivers.update({"Nile":"Egypt"})
rivers.update({"Dnieper":"Ukraine"})
rivers.update({"Don":"Russia"})
rivers.update({"Amazonka":"USA"})
rivers.update({"Yangtze":"China"})

for key,value in rivers.items():
    print("\nRiver "+key.upper()+" runs through "+value.upper()+".")

print("\n----------------------------------------------")
print("\nTask2: ")

for key in rivers.keys():
    print("\n"+"Key is: "+key.title())

for value in rivers.values():
    print("\n"+"Value is: "+value.title())

print("\n----------------------------------------------")
print("\nTask3: ")