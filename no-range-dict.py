    # Numbers 1 through 10 (generated with range())

square = {}
for i in range(1,11):
    square[i]= i ** 2
print(square)

    # using while loop

square = {}
num = 1
while num<=10:
    square[num] = num ** 2
    num = num + 1
print(square)