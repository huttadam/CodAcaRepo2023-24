my_dog = {"name": "Ted", "age":15, "breed": "Border Collie"}

my_dog['owner'] = "Matt" # adds key/value pair

print(my_dog)

print(my_dog.keys)

for k,v in my_dog.items():
    print(f"The value of {k} is {v}")

print(my_dog.get('', "unknown"))
