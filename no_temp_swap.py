# Swaps two variables without using a temp

a = 5
b = 8

print(a, b)

a = a + b
b = a - b
a = a - b

print(a, b)
