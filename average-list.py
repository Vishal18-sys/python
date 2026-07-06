# Find the average of list elements 

total=0
num=[1,2,3,4,5,6,7,8,9,10]
count= len(num)
for i in num:
    total= total + i
    average =  total / count
print("Average: ",average) 

# Another way to calculate average 

total = 0

num=[]
for i in range(5):
    number = int(input("Enter a number: "))
    num.append(number)
count = len(num)
for i in num:
    total = total + i
    avg = total / count
print("Average: ",avg)