num=12345
reverse=0
temp=num
while (temp>0):
    digit=temp%10
    reverse=(reverse*10)+digit
    temp=temp//10
    print(temp)
print(reverse)
