    # keep only scores greater than 60 
    # use dictionary comprehension

scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
passed = {key:val for  key,val in scores.items() if val>60 }
print(passed)

 