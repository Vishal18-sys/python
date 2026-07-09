    # Sum of all values in dictionary

expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
total = 0
 # using for loop 

for value in expenses.values():
    total = total + value
print("Total values of dict: ", total)

# normal way

total = sum(expenses.values()) 
print("The total value of dict: ", total)