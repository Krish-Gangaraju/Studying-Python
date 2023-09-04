str1 = str(input('Enter a palindrome if you want to (without any spaces) '))
len(str1)
a = 0
flag = 1
while a < len(str1)//2:
    if str1[a] != str1[-(a+1)]:
       flag = 0
        
    a = a+1
        

if flag == 1:
    print('It is a palindrome')
else:
    print('Not a palindrome')
    


        
    
        
        



