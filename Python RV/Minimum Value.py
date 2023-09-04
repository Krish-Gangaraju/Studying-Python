l1 = eval(input('Enter a list of numbers '))
print('You will get the minimum value of the list and the index')

length = len(l1)
if length >1:
     for i in range(0,length-1):
        if l1[0] > l1[1]:
            rem = l1.pop(0)
            index=i+1
        
        else:
            rem = l1.pop(1)
            index=i
        
print(l1,index)
elif length == 1:
    print('There is only one value so that is the minimun isn\'t it')
else:
    print('Ha that was a good effort')

