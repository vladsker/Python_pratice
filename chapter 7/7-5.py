number_of_visitors=0

while number_of_visitors<12:
    age = input("Dear visitor, please, tell me your age.\n\t\t")

    age = age.strip()

    if age:
        age = int(age)
    else:
        print("Error")
        break

    if age <= 5:
        number_of_visitors += 1
        print("You can have free ticket. Please, go.\n\t\tNext!")
        print(number_of_visitors)
        continue
    elif (age > 5 and age < 12):
        number_of_visitors += 1
        print(number_of_visitors)
        print("Your ticket is 12 euro.\n\t\tNext!")
        continue
    elif (age == 120):
        number_of_visitors += 1
        print(number_of_visitors)
        print("Are you still interested in those movies? Really?\n\t\t")
        continue

