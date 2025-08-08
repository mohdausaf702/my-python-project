def cal_sum(a,b):
    sum=(a+b)
    print(sum)
    return sum

cal_sum(2,4)
cal_sum(9,8)
cal_sum(12,45)

def cal_avg(a,b):
    sum=a+b
    avg=sum/2
    print(avg)
    return cal_avg

cal_avg(120,68)

def print_hello():
    print("hello")

print_hello()

def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/2
    print(avg)
    return avg

cal_avg(24,26,28)

def mul(a,b):
    m=a*b
    print(m)

mul(9,3)



def x(cities):
    print(len(cities))

cities=["Delhi","Noida","Paris"]
x(cities)

hero=["Spider man","Krish"]
cities=hero
x(cities)


hero=["Spider man","Krish"]

def print_len(lst):
    print(len(lst))

n=5
fact=1
for i in range(1,6):
    fact*=i
    print(fact)   


def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)

cal_fact(9)        

def cal_D(USD_INR):
    x=USD_INR*83
    print(x)

cal_D(9)


def con(USD_INR):
    x=USD_INR*83
    print(x)

city = ["Delhi", "Mumbai", "Paris", "Zurich"]

def length(city_list):
    length_value = len(city_list)
    print(length_value)

length(city)

city = ["Delhi", "Mumbai", "Paris", "Zurich"]

def x(city):
    x=len(city)
    print(x)
x(city)


city = ["Delhi", "Mumbai", "Paris", "Zurich"]
hero= ["Spidermen","Krrish"]
def x(list):
    print(len(list))

x(city)  
x(hero)

def cal(a,b):
    print(a*b)

cal(5,12)
cal(9,6)

def x(n):

    for i in range (n,n+1):
     if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")

x(589)     


hero=["Iroonman","Krish","Captain America"]
city=["Saharanpur","Paris","Switzerland"]
print(hero[0], end=" ")
print(city[0] ,end=" ")

hero=["Iroonman","Krish","Captain America"]
city=["Saharanpur","Paris","Switzerland"]
print(*hero,*city, sep=",")

i=1
while i<=10:
    if i%2!=0:
        print(i)
    i+=1

i=1
while i<=10:
    print(3*i)
    i+=1

i=1
while i<=5:
    print("Jamia")
    i+=1

n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
    print(fact)    

n=input(int("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact *=i
    print(fact)

n = int(input("Enter the number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
    print(fact)

i=1
while i<=10:
    print("jamia")
    i+=1

i=1
while i<=10:
    print(3*i)
    i+=1    

str="Apna"
    
x="Ausaf"
print("My name is :", x)    