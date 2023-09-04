num = int(input("Enter any number "))
if num==2:
    print("Number is prime")
else:
    for i in range(2,num):
        a = num%i
        if a == 0:
            print("Number is composite")
            break
    else:
        print("Number is prime")
