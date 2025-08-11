#       Lamda
# x = lambda a: a+20
# print(x(5))

# x= lambda  a,b: a+b
# print(x(5,80))

# double = lambda x:x*2
# print(double(5))

# cube = lambda x: x*x*x
# print(cube(5))

# avg= lambda x,y:(x+y)/2
# print(avg(3,5))

#          Filter


# def prime(x):
#     if x < 2:
#         return False
#     for n in range(2, x):
#         if x % n == 0:
#             return False
#     return True
#
#
# filtered = filter(prime, range(10))
# print("Prime numbers are:", list(filtered))

# l = [1, 2, 3, 4, 5, 6, 7, 8]
#
# def filter_function(a):
#     return a > 4
#
# newnewl = list(filter(filter_function, l))
# print(newnewl)

#           Map

# def square(x):
#     return x * x
#
# numbers = [1, 2, 3, 4, 5]
# listsquare = map(square, numbers)
# print(list(listsquare))

# def cube(x):
#     return x*x*x
# print(cube(21))

# l = [1, 2, 3, 4]
#
# def cube(x):
#     return x ** 3
#
# newl = list(map(cube, l))
# print(newl)

l = [1, 2, 3, 4, 5, 6, 7, 8]
newl = list(map(lambda x: x * x * x, l))
print(newl)