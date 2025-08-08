i=1
while i<=10:
    print(i)
    i+=1

i=1
while i<=10:
    if i%2==0:
     print(i)
    i+=1


# i=1
# while i<=20:
#     if i%2!=0:
#         print(i)
#     i+=1

i=1
while i<=10:
    if i%2==0:
        print(i)
    i+=1    

num=[1,2,3,4,5,6,7,8]
for x in num:
    print(x)

x=["Potato","Lady finger","Tomato","Mint"]
for el in x:
    print(el)

tup=(1,2,3,4,5,6,7,8)
for x in tup:
    print(x)

x='Jamia Millia Islamia'
for y in x:
    print(y)
else:
    print('end')  

x="Apna College"
for char in x:
    if char=="o":
        print("o Found")
        break
    print(char)
else:
    print('end')
 
y="Ausaf"
for char in y:
    if char== "u":
        print("u found")
        break
    print(char)
else:
    print("End")

x="Jamia" 
for y in x:
    if y=="a":
        print("a found")
        break
    
x=[1,4,9,25,36,49,64,81,100]
i=0
while i<len(x):
    if x[i]==4:
     print(x[i])
    i+=1

x=C
c=49
for y in x:
    if y==c:
        print(4)

x=[1,2,3,4,5,6]
m=2
for y in x:
    if y==m:
     print("find")

x=[1,4,9,25,36,49,64,81,100]
m=49
idx=0
for y in x:
    if y==m:
        print("find",idx)
        break
        idx+=1

for i in range(0,6,1):
    print(i)

for i in range(1,10,2):
    print(i)   
#  
seq=range(6) 
for x in seq:
    print(x)

for i in range(2,10):
    print(i)   

for i in range(2,10,2):
    print(i)

for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)

n=int(input("Enter the number:"))
for i in range(1,11):
    print(n*i)    

i=1
while i<=10:
    print(6*i)
    i+=1

for in in range(6):
    pass
print("some useful work")

n=5
for i in range(1,n+1):
    print(i)

p=1
for i in range(1,6):
    p*=i

n=5
sum=0
for i in range(1,n+1):
    sum*=i
    print(i)

n=5
sum=0
for i in range(1,n+1):
    sum+=i
    print(i)    

n=7
sum=0
i=1
while i<=n:
    i+=1
    print("sum=",sum)

n = 7
sum = 0
i = 1
while i <= n:   
    sum += i
    i += 1
    print("sum =", sum)

n=8
sum=0
i=1
# while i<=n:
#     sum+=i
#     i+=1
#     print("sum=",sum)

n=7
sum=0
for i in range(1,n+1):
    sum+=i
    print("total sum=", sum)   

n=9
sum=0
for i in range(1,n+1):
    sum+=i
    print("sum=",sum)

n=6
for i in range(1,n+1):
    sum+=i
    print(sum)

n=1
for i in range(1,6):
    n*=i
    print("n=",n)

n=6
sum=0
for i in range(1,n+1):
    sum+=i
    print("sum=",sum)

n=7
sum=0
for i in range(1,n+1):
    sum+=i
    print("sum=",sum)

n=6
product=1
for i in range(1,6):
    product*=i
    print(product)


n=5
fact=1
for i in range(1,n+1):
    fact*=i
    print(fact)

n=5
fact=1
while i<=n:
    fact*=i
    i+=1
    print(fact)               

n=5
fact=1
while i<=n:
    fact*=i
    i+=1
    print(fact)

n=6
sum=0
for i in range(1,n+1):
    sum+=i
    print(sum)  