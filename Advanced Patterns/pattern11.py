# 1
# 01
# 101
# 0101
# 10101

num = int(input("Enter Number : "))

for i in range(num):
    for j in range(i+1):
        if((i+j)%2==0):
            print("1",end="")
        else:
            print("0",end="")
    print() 