#1
#12
#123
#1234
#12345

num = int(input("Enter Your Number : "))

for i in range(1,num+1):
    for j in range(i):
        print(j+1,end="");
        j=j+1;
    print();