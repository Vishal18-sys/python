# Print star pattern 

num=int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(i,num+1):
        print("*",end=' ')
    print()

# Reverse Star Pattern

num=int(input("Enter a number: "))
for i in range(num+1,0,-1):
    for j in range(num+1,i,-1):
        print('*',end=' ')
    print()

# Square Pattern 

num=int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end=' ')
    print() 