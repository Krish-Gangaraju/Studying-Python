a = float(input("Enter the 1st number "))
b = float(input("Enter the 2nd number "))
c = float(input("Enter the 3rd number "))
if(a>b>c):
    print(a,b,c, sep = '...')
elif(a>c>b):
    print(a,c,b, sep = '...')
elif(b>a>c):
    print(b,a,c, sep = '...')
elif(b>c>a):
    print(b,c,a, sep = '...')
elif(c>a>b):
    print(c,a,b, sep = '...')
elif(c>b>a):
    print(c,b,a, sep = '...')
