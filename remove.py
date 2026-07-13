    # Remove None Values
data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
result = {k:v for k,v in data.items() if v is not None}
print(result)

    # Remove Values
data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
result = {k:v for k,v in data.items() if v is None}
print(result)