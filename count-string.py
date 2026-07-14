    #   Count the number of vowels in a string.

text=input("Enter a string: ")
count=0
for ch in text:
    if ch.lower() in "aeiou":
        count=count+1
        print(ch)
print("number of vowels in a string are: ",count)

    #   Count the number of consonants in a string.

text=input("Enter a string: ")
count=0
for ch in text:
    if ch.lower() not in "aeiou":
        print(ch)
        count=count+1
print("number of consonants in a string are: ",count)