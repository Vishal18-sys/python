# Write a program to print all even number between 1 to 100

num=int(input("enter number: "))
for i in range(1,num+1):
    if i%2==0:
        print("even number:",i)
print("End this code")



# Write a program to print all odd number between 1 to 100

num=int(input('enter number: '))
for i in range(1,num+1):
    if i%2!=0:
        print("Odd number:",i)
print("End this code")