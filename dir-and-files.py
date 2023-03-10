import os
import string

#1

path = str(input())

print("Only directories:")
for name in os.listdir(path):
    if os.path.isdir(name):
        print(name)


print("\nOnly files:")
for name in os.listdir(path):
    if not os.path.isdir(name):
        print(name)

print("\nAll directories and files :")
for name in os.listdir(path):
    print(name)

#2

path = str(input())
x = os.access(path, os.F_OK)
print('Exist:', x)

x = os.access(path, os.R_OK)
print('Readable:', x)

x = os.access(path, os.W_OK)
print('Writable:', x)

x = os.access(path, os.X_OK)
print('Executable:', x)

#3

path = str(input())

print("Exists: ")
print(os.path.exists(path))

print("\nFile name of the path:")
print(os.path.basename(path))

print("\nDir name of the path:")
print(os.path.dirname(path))

#4

with open("C:/Users/Admin/PycharmProjects/tsis-6/test.txt") as file:
    lines = len(file.readlines())
    print('Total Number of lines:', lines)

#5

list = input().split(' ')

with open("C:/Users/Admin/PycharmProjects/tsis-6/test.txt", "w") as file:
        for c in list:
                file.write("%s\n" % c)

x = open("C:/Users/Admin/PycharmProjects/tsis-6/test.txt")
print(x.read())

#6

for letter in string.ascii_uppercase:
    x = letter + ".txt"
    with open("C:/Users/Admin/PycharmProjects/tsis-6/" + x, "w") as file:
       file.writelines(letter)

#7

with open("C:/Users/Admin/PycharmProjects/tsis-6/test.txt") as file:
    with open("C:/Users/Admin/PycharmProjects/tsis-6/test-1.txt", "w") as file1:
        for line in file:
            file1.write(line)

#8

path = str(input())

if os.path.exists(path):
    os.remove(path)
else:
    print("No such file exists.")