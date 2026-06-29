# Write a program to find sum of all natural numbers between 1 to n
sum=0
num=int(input('enter number: '))
for i in range(1,num+1):
    sum=sum+i
    print(sum)
print("End code",sum)