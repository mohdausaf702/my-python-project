print("Mohd Ausaf")
print("My age is 25")

print("Mohd Ausaf.","My age is 25")

name="Ausaf"
age=24
c=23.5
print(name)
print(age)
print(c)

print("My name is:", name)
print("my age is:", age)

name="Ausaf"
age=25
c=24.8
print(type(name))
print(type(age))
print(type(c))

Name1='Ausaf '
Name2="Ausaf"
Name3='''Ausaf'''
print(Name1)
print(Name2)
print(Name3)

age=23
old=False
c=None
print(age)
print(old)
print(c)

a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a%b)
print(a//b)

a=10
b=10
print(a==b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a!=b)

num=10
num+=10
print(num)

num=10
num*=10
print(num)

a=10
b=5
print((a==b) or (a>b))
print((a==b) and (a>b))

a=2
b=2.6
print(a+b)

a=int("5")
b=2.6
print(a+b)

name=input("My name is:")
print( name)

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("Sum of number:", x+y)

side=float(input("Enter the side of square:"))
print("area of square:", side*side)

Num1=float(input("Enter first number:"))
Num2=float(input("Enter the second Number:"))
print("Average of number=", (Num1+Num2)/2)

a=int(input("Enter first the numbe:"))
b=int(input("Enter the second number:"))
print(a>=b)


                                                #  L2 string

x="This is string"
print(x)

x="My name is Ausaf \n I did my graduation \t from  Roorkee "
print(x)

x="Mohd"
y="Ausaf"
print(x+"  "+y)

x="Ausaf"
print(len(x))

x="Apna college"
print(x[0:len(x)])

x="Apple"
print(x[-5:])

x=input("Enter the Name:")
print("length of the string", len(x))

x= "$ is the currency $ of USA"
print(x.count("$"))
x="Apna College"
print(x.find("A"))
print(x.capitalize())
print(x.title())
print(x.lower())
print(x.upper())
print(x.swapcase())
print(x.title())
print(x.replace("Apna","My"))

x=int(input("Enter the number:"))
if x%2==0:
    print("Even number")
else:
    print("Odd Number")

x=int(input("Enter the number:"))
if x%7==0:
    print("multiple of seven")
else:
    print("Not multiple")

print("Hello World")    

                                #    Loops

i=1
while i<=5:
    print(i)
    i+=1

i=1
while i<=10:
    print("Jamia",i)
    i+=1

i=5
while i>=1:
    print(i)
    i-=1

i=1
while i<=10:
    print(4*i)
    i+=1

n=int(input("enter table of:"))
i=1
while i<=10:
    print(n*i)
    i+=1

nums=[1,2,3,4,5,6,7,8]
idx=0
while idx<len(nums):
    print(idx)
    idx+=1

nums=[1,2,3,4,5,6,7,8]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1

i=1
while i<=5:
    print(i)
    if i==3:
        break
    i+=1


i=1
while i<=8:
    if i==6:
        i+=1
        continue
    print(i)
    i+=1  

x=[1,2,3,4,5,6,7,8]
for i in x:
    print(i)

x="apple"
for i in x:
    print(i)

x="Apple"
for i in x:
    if i=="p":
     print("Found")

x=1,2,3,4,5,6,7,8
for i in x:
    print(i)

x= "Apna College"
for i in x:
    if i=="o":
        print("Found")

x=[1,2,3,4,5,6,7,8,90,20,30,30]
for i in x:
    print(i)

x=[1,2,3,4,5,6,7,8,90,20,30,30]
j=5
for i in x:
    if i==j:
        print("number found")

for i in range(1,100):
    print(i)


for i in range(1,100,2):
    print(i)

for i in range(1,11):
    print(9*i)

for i in range(10,0,-1):
    print(i)

for i in range(1,11,1):
    print(i)

n=int(input("Enter the table:"))
for i in range(1,11):
    print(n*i)

n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

                                    #   Function

def cal(a,b):
    print(a+b)

cal(198,765)

def cal(a,b):
    print(a*b)

cal(9,8)    

def cal(a,b,c):
    print((a+b+c)/3)

cal(9,9,9)    

cities=["Delhi","Mumbai"]

def x(list):
    print(len(list))

x(cities)

cities=["Delhi","Mumbai"]
hero=["ironman","Thor"]

def x(list):
    for item in list:
        print(item,end=" ")
        x(hero)

def cal(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

cal(8)

def converter(INR_USD):
    print(INR_USD*83)

converter(2) 


print("Hello World")

                                #  List and Tuples

marks=[89,98,92,96,74,94]
print(marks)
print(type(marks))
print(marks[0])
print(len(maarks))

Student=["Ausaf",94,89.6,"Delhi"]
Student[3]="Mumbai"
print(Student)

Student=["Ausaf",94,89.6,"Delhi"]
print(Student[0:2])

Student=["Ausaf",94,89.6,"Delhi"]
Student.append("Pune")
print(Student)

Student=["Ausaf",94,89.6,"Delhi",1]
Student.sort
print(Student)

list=[1,4,5,3,8,5]
list.sort()
print(list)

list=[1,4,3,8,5]
list.sort(reverse=True)
print(list)

list=[1,4,3,8,5]
list.remove(4)
print(list)

list=[1,4,3,8,5]
list.insert(0,98)
print(list)

list=[1,4,3,8,98]
list.sort()
print(list)

list=[1,4,3,8,5]
list.pop(0)
print(list)


print("Hello World")

                                    #  tuples

x=(1,2,3,4,5)
print(x)
print(type(x))
print(x[2:4])

tuple=(1,2,2,3,4,5)
print(tuple.index(1))
print(tuple.count(2))

movies=[]
movies.append(input("Enter the 1 movies name"))
movies.append(input("Enter the 2 movies name"))
movies.append(input("Enter the 3 movies name"))
print(movies)

list=("a","m","j","a")
print(list.count("a"))

x=["a","m","j","a","b","c"]
x.sort()
print(x)

list1 = [1, 2, 1]

# Make a copy and reverse it
copy_list1 = list1.copy()
copy_list1.reverse()

# Check if list1 is a palindrome
if list1 == copy_list1:
    print("Palindrome")
else:
    print("Not palindrome")

print("Hello world")



