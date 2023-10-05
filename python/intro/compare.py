import math

# x =int(input("What is X? "))
# y =int(input("What is Y? "))


# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")



# name =(input("What is your name? "))

# match name:
#     case "harry" | "ron" | "hermione" :
#         print("Gryfinndor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Mudblood")   


shape =(input("What is your shape? "))


match shape:
    case "square":
        square_vert = (input("What is your vertical length"))
        square_hori = (input("What is your horizontal length"))
        print(f" the surface area of your {shape} is { square_vert * square_hori}")
    case "triangle":
        tri_base = float((input("What is your base")))
        tri_height = float((input("What is your length")))
        print(f" the surface area of your {shape} is { 0.5 * tri_base * tri_height}")
    case "circle":
        rad = float((input("What is your radius")))
        print(f" the surface area of your {shape} is { math.pi * rad * rad}")