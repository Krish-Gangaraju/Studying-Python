fact = float(input('Enter a positive whole number '))
ans = 1

while fact > 0:
    ans = ans*fact
    fact = fact-1
print(ans)
