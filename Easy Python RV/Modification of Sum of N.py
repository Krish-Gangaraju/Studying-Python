n = float(input("Enter any amount of numbers as you want "))
sum = (n+1)/2
sum = sum*n
print("The sum of all these numbers before this is ",sum)
print('Would you like to repeat')
a = str(input('yes or no '))
while a == 'yes':
    n = float(input("Enter any amount of numbers as you want "))
    sum = (n+1)/2
    sum = sum*n
    print("The sum of all these numbers before this is ",sum)
    a = str(input('yes or no '))
print('This is the end of the program')




