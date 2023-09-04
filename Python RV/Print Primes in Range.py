num = int(input("Enter a number to get all the primes before it(2-100) "))
prime = []
for i in range(2,num):
    for b in range(2,i):
            if i%b == 0:
                break
    else:
         prime.append(i)    
print(prime)
            
            

