for i in range (10,1001):
    num=i
    count=len(str(num))
    add=0
    temp=num
    while (temp>0):
        digit=temp%10
        power=digit**count
        add=add+power
        temp = temp // 10
    if (add==num):
        print(num, "is Armstrong")
