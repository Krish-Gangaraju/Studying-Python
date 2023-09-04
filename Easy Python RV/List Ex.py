l = eval(input('Enter a list of numbers starting with [] and commas seperating the numbers '))
length = len(l)
n = 0
m = 0
count = 1
uni = []
dup = []

while n < length:
    m = n+1
    count = 1
    i=0  #changed it to 0 otherwise it was not checking first element in dup
    while i < len(dup):
        if l[n]==dup[i]:
           # n = n+1
           # m=n+1
            break
        i+=1
    else:
            while m < length:
                
                if l[n] != l[m]:
                    m = m+1
                else:
                    count = count+1
                    m = m+1
                    
            if count > 1:
                dup.append(l[n])   
            else:
                uni.append(l[n])   
            print(l[n],'   ',count,'times')
    n = n+1
            
print("Original List",l)
print('These are the duplicates ',dup)
print('These are unique  ',uni)
#[9,2,1,6,8,5,1,2,2,9,3,8]

