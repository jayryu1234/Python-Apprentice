c = "Hello"
l = ['a','a','b','b','c','c']

# Make a tuple from a list
t = tuple(l)
print(t)

# Make a set from a list
s = set(l)
print(s)

# Make a list from a string
a = list(c)
print(a)

# Get the unique items from a list, by converting it to a set
# and then back to a list
print(list(set(l)))