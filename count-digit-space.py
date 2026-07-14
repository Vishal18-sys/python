    # Count the number of digits in a string.

text=input("Enter a string: ")
count=0
for ch in text:
    if ch.isdigit():
        print(ch)
        count=count+1
print("he number of digits in a string are: ",count )

    # Count the number of spaces in a string.

text=input('Enter a string: ')
count=0
for ch in text:
    if ch.isspace():
        count=count+1
print("the number of spaces in a string are: ",count)