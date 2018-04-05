with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('pi_digits.txt') as file_object:
    for i in file_object:
        print(i.rstrip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    print(lines)

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_million_string = ''
for line in lines:
    pi_million_string += line.strip()

print(pi_million_string)
print(len(pi_million_string))

birthday = input("Please, type your birthday ")
if birthday in pi_million_string:
    print("Yes!")
else:
    print("No!")