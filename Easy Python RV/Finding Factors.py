num = int(input('Enter a number to find out its factors '))
a = num/2
p = 1
i = 0
list1 = []

while p <= a :
    if num%p == 0:  
       list1.append(p)
       i = i+1
    p=p+1
list1.append(num)
print(list1)
ans = str(input("If you want to continue press x "))
while ans == 'x':
    num = int(input('Enter a number to find out its factors '))
    a = num/2
    p = 1
    i = 0
    list1 = []

    while p <= a :
        if num%p == 0:  
           list1.append(p)
           i = i+1
        p=p+1
    list1.append(num)
    ans = str(input("If you want to continue press x "))
print('This is the end of the program')




