num=153
count=len(str(num))
add=0
temp=num
while (temp>0):
    digit=temp%10
    power=digit**count
    add=add+power
    temp = temp // 10
print(add) 
if (add==num):
    print(num, "is Armstrong")  
else:
    print(num, " is not Armstrong")
