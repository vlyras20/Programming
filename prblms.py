print ("PROBLEM 1")
words = ["xxx", "aaa", "r5t6yy", "g", "wow"]

for l in words:
    if len(l) >= 2 and l[0] == l[-1]:
        print (l)

print ("PROBLEM 2")
number = int(input("Gimme a number: "))
numbers = [2, 3, 5, 7, 66, 89, 134]

for n in numbers:
    if number > n:
        print (n)

print ("PROBLEM 3")

nestedL = [1, [2,3], [4,5,6], [7,8,9,10]]

print (nestedL, end = "")
