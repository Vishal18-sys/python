    # Sort Dictionary by Values
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
result = dict(sorted(scores.items(), key=lambda item: item[1]))
print(result)

    # Sort Dictionary by Values in reverse order
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
result = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True)) 
print(result)