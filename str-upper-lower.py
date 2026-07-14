    # Count the number of uppercase letters.

text=input("Enter a string: ")
count = 0
for ch in text:
    if ch.isupper():
        print(ch)
        count=count+1
print("the number of uppercase letter is: ",count)

    # Count the number of lowercase letters.

text = input("Enter a string: ")
count=0
for ch in text:
    if ch.islower():
        print(ch)
        count=count+1
print("the number of lowercase letter is: ",count)