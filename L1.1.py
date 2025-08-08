print("mY NAME IS AUSAF")
print("My age is 24")

print("mY NAME IS AUSAF","My age is 24")

name="Ausaf"
age=24
price="24.5"
print(name)
print(age)
print(price)

name="Ausaf"
age=24
price="24.5"
print("My name:",name)
print("my age is:",age)
print("price is:",price)

print(type(name))
print(type(age))
print(type(price))

age=23
old=False
a=None
print(type(age))
print(type(old))
print(type(a))

a=1
b=2
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)
print(a//b)
print(a%b)

a=50
b=20
print(a==b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)

num=10
num=10+num
print(num)

num=10
num*=10
print(num)

a=50
b=40
print((a<b) and (a>b))
print((a>b) or (a<b))

a=1.j
x=int(a.imag)
print(x)

a=2
b=2.48
print(a+b)

a=int(4.45)
print(a)

name=input("my name is:")
age=input("my age is:")
marks=input("my marks is:")

first=int(input("My first number:"))
second=int(input("my second number is:"))
print("sum", first+second)

side=float(input("Enter the side:"))
print("side od square:", side*side)

a=int(input("enter the number:"))
b=int(input("enter the number:"))
print(a>

                     #L2

x="This my my college"
y="apna college"
z="This is string"  
print(x)
print(y) 
print(z)                                   

x="Mohd"
y="Ausaf"
print(x+" "+y)


x="apna college"
print(x[1:len(x)])


x="ausaf"
print(x[:2])

x="Real Data"
print(x[-4:-1])

x="Ausaf"
print(len(x))
print(x.capitalize())
print(x.find("a"))
print(x.swapcase())
print(x.replace("A","a"))
print(x.title())

name=input("Enter the name:")
print("length of the name", len(name))

x=  " dollar is $ the currency of $"
print(x.count("$"))

                                    #Function

def sum(a,b):
    print(a+b)

sum(6,8)

def product(a,b):
    print(a*b)

product(9,8)    

def word():
    print("hello world")

word()
word()
word()
word()
word()
word()


def sum(a,b):
    print(a+b)

sum(6,8)
sum(7,8)
sum(9,0)
sum(8,76)


def sum(a,b,c):
    print((a+b+c)/3)

sum(9,8,6)    


city=["Delhi","Gurgaon","Mumbai"]

hero=["Spider men","Iron men","Krrish"]
 
def x(cities):
    print(len(cities))

x(city)
x(hero)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

factorial(9)
factorial(10) 
factorial(7)
factorial(6) 


def converter(INR_USD):
    print(INR_USD*83)

converter(2)

                                                   Conditional Statement

age=25
if age >=18:
    print("can vote")
    print("can drive")

light = "green"
if light == "Red":
    print("stop")
elif light =="yello":
    print("look")
elif light=="green":
   print("go")

light = "Pink"
if light == "Red":
    print("stop")
elif light =="yello":
    print("look")
elif light=="green":
   print("go")
else:
    print("light is broken")

n=5
if n>2:
    print("n is greater than 2")
elif n<6:
    print("n is smaller than 6")

marks=int(input("Enter the marks:"))
if marks >=90:
    grade="A"
elif marks >=80 and marks <90:
    grade="B"
elif marks >=70 and marks <80:
    grade="C"
else:
    grade="D"

print("Grade of student:", grade) 

n=int(input("Enter the number:"))
if n%2==0:
    print("number is even")
else:
    print("can not even")   

n=int(input("enter the number of:"))
if n %2 ==0:
    print("multiple of 7")
else:
    print("can not multiple 7")

                                        Loops
i=1
while i<=5:
    print(i)
    i+=1

i=1 
while i<=5:
    print("Hello")
    i+=1

i=6
while i>=1:
    print(i)
    i-=1

i=1
while i<=10:
    print("Jamia",i)
    i+=1

i=1
while i<=100:
    print(i)
    if i==50:
        break
    i+=1

i=1
while i<=100:
    if i==50:
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    print(3*i)
    i+=1

x=[1,2,3,4,5,6,7,8]
idx=0
while idx <= len(x):
    print(idx)
    idx+=1

nums=[1,2,3,4,5,6,7,8]
x=6
i=0
while i<len(nums):
    if nums[i]==x:
     print("found at idx",i)
    i+=1

i=1
while i<=6:
    print(i)
    if i==4:
        break
    i+=1

i=1
while i<=6:
    if i==4:
        i+=1
        continue
    print(i)
    i+=1

x=[1,2,3,4,5,6]
for i in x:
    print(i)

x= "apna college"
for i in x:
    if i=="o":
        print("o found")

x=[1,2,3,4,5,6]
z=6
for i in x:
    if i==z:
     print("found")

for i in range(2,10):
    print(i)

for i in range(100,0,-1):
    print(i)   

n=2
for i in range(1,11):
    print(2*i)

n=5
for i in range(1,n+1):
    print(i)

n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum", sum)

n=7
sum=0
i=1
while i <=n:
    sum+=i
    i+=1
    print(sum)

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial",fact)

n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)

print("hello world")


x=10
y=2.0
z=3j
print(type(x))
print(type(y))
print(type(z))

x=5
y="John"
print(x)
print(y)

x=int(5.0)
print(x)

x=8j
c=int(8j.imag)
print(x)

x,y,z= "Cherry","apple","Pineapple"
print(x)
print(y)
print(z)

x=y=z="Oranges"
print(x)
print(y)
print(z)

x="""oranges are 
orange in 
colour
"""
print(x)


x="hello world"
print("hello" in x)

x="hello world"
print(x.upper())
print(x.lower())
print(x.swapcase())
print(x.title())
x="hello"
y="world"
print(x+"  "+y)

a=2
b=10
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

a=20
b=20
if a >b:
    print("a is greater than b")
elif a==b:
    print("equal to")

def cal():
    print("hello world")

cal()

def cal(x):
    print(x+"  "+"world")
cal("yello")

x=[1,2,3,4,5,6,7,8]
for i in x:
    print(i)

x="Fruit"
for i in x:
    print(i)

x=[1,2,3,4,5,6,7,8]
for i in x:
    print(i)
    if i==4:
        break

x=[1,2,3,4,5,6,7,8]
for i in x:
    if i==5:
        continue
    print(i)

i=1
while i<=6:
    print(i)
    if i ==4:
        break
    i+=1


i=0
while i<=6:
    i+=1 
    if i==4:
     continue
    print(i)   


                               list and Tuple (Additional)

x=[1,2,3,4,5,6,7,8]
print(x)
print(x[2:5])

student=["Ausaf",94,18,"Delhi"]
student[0]="Rahul"
print(student)

student=["Ausaf",94,18,"Delhi"]
student.append("Mumbai")
print(student)

list=[1,2,3,4,5,6,7,8]
list.sort()
print(list)

list=[1,2,3,4,5,6,7,8]
list.reverse()
print(list)
list.sort(reverse=True)
print(list)

list.insert(4,"Mumbai")
print(list)

list=[1,2,3,4,5,6,7,8]
list.insert(6,99)
print(list)

x=("aplle")
x=(("Mango")+" "+ (x))
print(x)

tuple=(1,2,3,4,5,6,7,)
print(tuple)
print(tuple[2:5])
tuple.index(1)

tuple=(1,2,3,4,5,6,7,)
print(tuple.count(2))
print(tuple.index(2))

movies=[]
movies.append(input("enter the number of movies 1:"))
movies.append(input("enter the number of movies 2:"))
movies.append(input("enter the number of movies 3:"))
print(movies)

list=("m","a","a","m","p")
print(list.count("a"))

list=["A","C","D","B"]
list.sort()
print(list)

print("Hello World")