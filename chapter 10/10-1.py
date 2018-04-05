filename = "learning_python.txt"
lines=[]
new_lines = []

with open(filename) as file_object:
    print(file_object)
    lines = file_object.readlines()

print(lines)
print(len(lines))
print(lines[1].title())

for i in range(0,len(lines)-1):
    new_lines.append(lines[i].replace("Python", "C"))

print(new_lines)