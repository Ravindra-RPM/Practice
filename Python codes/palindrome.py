num = 765
temp=num
newnum=''
while(num>0):
    r = num % 10
    newnum += str(r)
    num = num // 10
    
print(newnum)
if temp == int(newnum):
    print(f"{temp} is a palindrome")
else:
    print("Not palindrome")