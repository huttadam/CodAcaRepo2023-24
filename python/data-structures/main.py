from my_module import person,s,foo as bar,person,y

# imported from my_module and named as something else.

# print(my_module)
# print(dir(my_module)) # gives information on whats inside and directory


def foo(x):
    print(x)

# print(person)
# print(s)

foo(person)


# bar used as foo
bar(s)

print(dir())

# print(y)

