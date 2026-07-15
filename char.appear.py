    # Count how many times a given character appears
text=input("Enter a string: ")
char=input("Enter a character: ")
count=0
for ch in text:
    if ch==char:
        count=count+1
print("character appears in that time: ",count)