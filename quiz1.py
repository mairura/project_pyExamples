# recursive function
def my_func(x):
    if x == 0:
        return 0
    else:
        return x + my_func(x-1)


print(my_func(4))

# Operator precedence
x = 2
y = 10
x *= y * x + 1
print(x)

# This prints out the dictionary key value items
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(key, value)

for i in range(3):
    for j in range(3):
        print(i, j)
