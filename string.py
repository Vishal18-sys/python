    # Create a string and print it.

str='hello buddy'
print(str)
    # Take a string as input from the user and print it. and also print the length of string 

str=input("Enter a name: ")
print(str)
print(len(str))
    
    # Print the first character of a string.

str='hello buddy'
print(str[0])
    # Print the last character of a string

str='hello buddy'
print(str[-1])

    # Print all characters of a string using a for loop.

text = input("Enter a string: ")
for str in text:
    print(str)    

    # Print a string in reverse.

text = input("Enter a string: ")
print(text[::-1])

    # Convert a string to uppercase.

text = input("Enter a string: ")
for str in text:
    print(str.upper())

    # Convert a string to lowercase.

text = input("Enter a string: ")
for str in text:
    print(str.lower())

    # Count the number of characters in a string without using len().

text=input("Enter a string: ")
count=0
for i in text:
    count = count + 1
print("len of Str: ",count)
    
    # Print each character of a string on a new line.

str=input("enter a string: ")
for i in str:
    print(i)

    # Print characters at even indexes.

text=input("Enter a string: ")
for i in range(len(text)):
    if i%2==0:
        print(text[i])

    # Print characters at odd indexes.

text=input("Enter a string: ")
for i in range(len(text)):
    if i%2!=0:
        print(text[i])

   