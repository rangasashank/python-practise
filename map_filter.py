#---------------MAP-----------------#

# numbers = ["3","34","64"]

# numbers = list(map(int, numbers))


# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i])


# numbers[2] = numbers[2] + 1
# print(numbers[2])

# # def sq(a):
# #     return a*a

# num = [2,3,4,5,6,7,8,9]
# square = list(map(lambda x: x*x, num))
# print(square)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square,cube]

# for i in range(10):
#     val = list(map(lambda x:x(i), func))
#     print(val)



# -------------------FILTER-------------#

# list1 = [1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num > 5

# greaterthan5 = list(filter(is_greater_5, list1))
# print(greaterthan5)

#----------------------REDUCE----------------------#

from functools import reduce
list1 = [1,2,3,4,5,6,7,8,9]
num = reduce(lambda x,y:x+y, list1)
print(num)