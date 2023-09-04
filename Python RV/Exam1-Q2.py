l = str(input("Enter any string "))
length = len(l)
print(length)
n = 0
vowel = ['a','e','i','o','u']
while n <= length:
    if l[n] in vowel:
        break
    else:
        n = n+1
print(l,"ay")

    
