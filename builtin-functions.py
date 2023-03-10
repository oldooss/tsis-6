#1

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply((8, 2, 3, 1, 7)))

#2

def string_test(text):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in text:
        if c.isupper():
           d["UPPER_CASE"] += 1
        elif c.islower():
           d["LOWER_CASE"] += 1
        else:
           pass
    print ("Original String : ", text)
    print ("Upper case characters : ", d["UPPER_CASE"])
    print ("Lower case Characters : ", d["LOWER_CASE"])

string_test(' Labka 6 ezhe ')

#3

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print(isPalindrome('aza'))

#4

from time import sleep
import math

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)


x = int(input("First num: "))
y = int(input("First num: "))

print(f"Square root of {x} after {y} miliseconds is")
print(delay(lambda x: math.sqrt(x), 2123, 25100))

#5

x = (True, True)
print(all(x))








