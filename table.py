# Write a program to print tables

num=int(input('enter number: '))
for i in range(1,11):
    print(num,'*',i,'=',num*i)
print("table end")

# Write a program to print reverse tables

num=int(input("enter number: "))
for i in range(10,0,-1):
    print(num,'*',i,'=',num*i)
print("reverse table")