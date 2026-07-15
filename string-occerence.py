    # Find the first occurrence of a given character

text=input("Enter a string: ")
char=input("Enter a character: ")
index=-1
for ch in range(len(text)):
    if text[ch]==char:
        index=ch
        break
print("the first occurrence of a given character: ",index)

    # Find the last occurrence of a given character

text=input("Enter a string: ")
char = input("Enter a character: ")
index=-1
for ch in range(len(text)):
    if text[ch]==char:
        index=ch
print("The last occurrence of a given characte: ",index)