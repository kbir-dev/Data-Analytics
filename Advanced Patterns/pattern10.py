# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

num = int(input("Enter Number : "))

for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(num):
    for j in range(num-i):
        print("*",end="")
    print()