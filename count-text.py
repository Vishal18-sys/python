 # Word Count in text using split()

text = "the cat sat on the mat the cat"
word={}
for count in text.split():
    word[count] = word.get(count,0)+1
print(word)