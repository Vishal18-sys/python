# Write a program to find the factorial value of any number

fact=1
num=int(input('Enter  number: '))
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("The factorial 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
print("Factorial of number is:",fact)