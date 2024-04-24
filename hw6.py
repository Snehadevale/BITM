'''name = "\u0cb8\u0ccd\u0ca8\u0cc7\u0cb9"  
print(name)'''


'''a=5
b=7
c=9
d=34
e=90
print('a' if a>b and a>c and a>d and a>e else 'b' if b>c and b>d and b>e else 'c' if c>d and c>e else 'd' if d>e else 'e')'''

'''print(chr(3206)+chr(3205))
print(ord('a'))'''

'''for i in range(ord('A'),ord('Z')):
    print(ord(chr(i)),end=' ')'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()'''

'''for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()'''

'''i=1
while i<6:
    j=1
    while j<=i:
        print('*',end=' ')
        j=j+1
    print()'''


'''for i in range(1,11):
    print(i/10,end=' ')'''

'''name = "Sneha"
formatted_name = ""
for letter in name:
    formatted_name += letter + " "
formatted_name = formatted_name.strip()
print(formatted_name)'''

name = "Sneha"
length = len(name)
for i in range(length):
    for j in range(length):
        if i == j or i + j == length - 1:
            print(name[j], end=' ')
        else:
            print(' ', end=' ')
    print()


    
