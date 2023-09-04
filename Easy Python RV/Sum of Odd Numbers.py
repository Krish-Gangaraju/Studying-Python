num = int(input("Enter any number "))
sum = 0
if (num%2 == 0):
    num = num-1
    while num > 0:
        sum += num
        num = num-2
    sumf = sum-num
    print(sumf - 1)
else:
    while num > 0:
        sum += num
        num = num-2
    sumf = sum-num
    print("The sum of all the odd numbers",sumf - 1)
