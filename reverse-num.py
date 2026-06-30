# write a program to reverse the given Digits

reversed=0
num=int(input("Enter number: "))
while num>0:
    digit= num%10
    reversed= reversed*10 + digit
    num = num//10
print("Reverse number is :",reversed)