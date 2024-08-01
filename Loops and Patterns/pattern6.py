num = int(input("Enter Number : "))

for i in range(num):
    for j in range(1 , num + 1 - i):
        print(j,end="")
    print()