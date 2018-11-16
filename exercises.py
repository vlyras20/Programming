# #EXERCISE 2
# date = input("gimme a date in the form dd/mm/yyyy: ")
# monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#
# day, month, year = date.split('/')
#
# if day > 31 or month > 12:
#     print("Invalid Date")
#
# month = monthName
# print(day, monthName, year)

#EXERCISE 1 LISTS REVIEW
# a_list = [3, 5, 6, 12]
# b_list = []
# c_list = []
# d_list = []
# e_list = []
#
# for x in a_list:
#     if x < 4:
#         b_list.append(x)
# print(b_list)
#
# for x in a_list:
#     if x > 4:
#         c_list.append(x)
# print(c_list)
#
# print(sorted(a_list, reverse=True))
#
# for x in a_list:
#     d_list.append(x*3)
# print(d_list)
#
# for x in a_list:
#     if x%2 == 0:
#         e_list.append('True')
#     else:
#         e_list.append('False')
# print(e_list)

#EXERCISE 2
# List = []
# newList = []
#
# numbers = (input("gimme a list of numbers: ")
#
# numbers.append(List)
# numbers.split(" ")
#
# for n in numbers:
#     if n%2 == 0:
#         newList.append((int)n)
#     else:
#         List.append(n)
#
# print(List)
#
# #EXERCISE 3
# myList = [“axe”, “dagger”, “oranges”]

my_dict = {'item' : 4, 'item' : 5, 'item' : 6}
new_dict = {}

new_dict[i:v*2 for i,v in my_dict.items()

print(new_dict)
