# Write a program to find sum of all even numbers between 1 to n

num=int(input("enter number: "))
sum=0
for i in range(1,num+1):
    if i%2==0:
        sum=sum+i
        print("Sum of even no:",sum)
print("End this code")

# Write a program to find sum of all odd numbers between 1 to n

num=int(input('enter number:'))
sum=0
for i in range(1,num+1):
    if i%2!=0:
        sum=sum+i
        print('sum of odd no:',sum)
print("End this code")