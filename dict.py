    # Print dictionary or name
'''student = {"name": "Alice", "age": 20, "grade": "B"}
print(student)
print(student['name'])'''

    # Print dict item or pop the color

'''car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
car.pop('color')
print(car)
print(car.items())

print("'brand' is exist: ",'brand' in car)
print("'model' is exist: ",'model' in car)
print("'Latest' is exist: ",'Latest' in car)'''

    # Print add the value of keys or merge 

'''keys = ["name", "age", "city"] 
values = ["Bob", 25, "London"]
print(len(keys))
print(len(values))
#keys.extend(values)
person = dict(zip(keys,values))
print(person)
#print(keys)'''

    # Clear the dictionary

'''inventory = {"apples": 10, "bananas": 5, "oranges": 8}  # clear this dictionary
inventory.clear()
print(inventory)'''

    # merge dict1 and dict2

'''dict1 = {"a": 1, "b": 2}    # mergi dict1 and dict2
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)         # fiste method
print(dict1)

merge= dict1 | dict2        # Second method | operator is merge operator in dict
print(merge)'''

    # Access nested value in dict
    
'''person = {"name": "Carol", "address": {"city": "Paris","zip": "75001"}} # Access nested value in dict
print(person['address']['city'])'''

'''student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
result=student['grades']['history']
print("history grade = ",result)'''