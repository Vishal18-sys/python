# Write a program to swap two no. using two variable

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(f"Original number of a = {a} and b = {b}")
a = a + b 
b = a - b
a = a - b
print(f"Swap the number and the value of a={a} and b={b}")