sent = str(input("Enter a sentence "))
l = list(sent)
length = len(sent)
print(length)
count = 0
for i in range(0,length):
    if ' ' in l[i]:
        l.insert(i+1 ,"::")
        l.pop(i)
        count = count+1        
print(l)
print(count)
        
               

