'''apple=[10,5,30]
print(apple)
print(apple[1])
print(apple[-1])
print("for itteration via acces element")
for i in apple:
    print(i)

apple[1]=-100
print(apple)'''

'''bannana=[10,'balaji',25000.75,'z']
print(bannana)
for i in bannana:
    print(i,end="-")'''

'''a=[10,34,67,354,87]
print(a[-1])
print(a[:1])
print(a[1:])'''

'''a=[]
n=int(input('enter the list size'))
for i in range(0,n):
    ele=int(input("enter the element"))
    a.append(ele)
print(a)'''


'''a=[10,20,30,40,50]
b=[20,60,70,80,90,100]
c=a+b
print(c)
for i in a:
    for j in b:
        if(i==j):
            print(j)'''

'''for i in range(1,10,2):
    print(i+1)'''

'''a=(1,2,3,4)
print(a)
print(max(a))
print(min(a))
print(len(a))
print(a[-1])
print(a[:1])
print(a[1:4])
print(a[-1:-4])
print(a[1:10:2])'''


'''def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
values = []
for in range(5):
    value = float(input("Enter a number: "))
    values.append(value)
for value in values:
    if is_prime(value):
        print(f"{value} is a prime number.")
    if is_leap_year(value):
        print(f"{value} is a leap year.")'''

dict=dict([(4,'ram'),(2,'sita')])
print("\n dictionary e=with each item pair")
print(dict)
print(type(dict))

