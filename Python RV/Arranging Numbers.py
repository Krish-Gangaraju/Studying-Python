nums = eval(input("Enter 10 different numbers seperated by commas "))
check = 0
length = len(nums)
for check in range(0,length-1):
    final = check+1
    while final < length:
        if (nums[check] > nums[final]):           
            a,b = nums[check],nums[final]
            nums[check],nums[final] = b,a          
        final = final+1
print(nums)
            
