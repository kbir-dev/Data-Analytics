# *********
#  *******
#   *****
#    ***
#     *

num = int(input("Enter Your Number : "))

for i in range(num):
    for j in range(i):
        print(" ",end="")
    for j in range(2 * (num - 1 - i) + 1):
        print("*", end="")
    print()