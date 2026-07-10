    # Key of Minimum Value
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
lower = min(stock, key=stock.get)
print(lower)

    # Key of Maxmum and Minimum Value

scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
higher = max(scores , key=scores.get)
lower = min(scores, key=scores.get)
print(lower)
print(higher)