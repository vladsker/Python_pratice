sandwiches = {
    1: "salmon",
    2: "tuna",
    3: "beef",
    4: "pork",
    5: "pastrami",
    6: "pastrami",
    7: "pastrami"
}

#pastrami burgers deleting code

print("We are running out of pastrami. Unfortunately, we need to remove those burgers.")

pastami_keys=[]


for i in sandwiches.keys():
    if sandwiches[i] == "pastrami":
        pastami_keys.append(i)

for i in pastami_keys:
    del sandwiches[i]

eaten_sandwiches_counter = 0
eaten_sandwiches={}

while sandwiches:

    print("\n\nSandwiches I have are: ")

    for i,j in sandwiches.items():
        print(str(i) + " - "+ j + "\n")

    value = input("Which sandwich you want? \n")

    if value.strip():

        value=int(value)
        eaten_sandwiches_counter += 1
        eaten_sandwiches[eaten_sandwiches_counter]=sandwiches[value]

    else:
        print("=== no input ===")
        break

    if value in sandwiches.keys():
        del sandwiches[value]

print(eaten_sandwiches)
