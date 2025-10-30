
x = "I am divisible by 3 and 5!"
y = "I am divisible by just 3!"
z = "I am divisible by just 5!"

max_number=100

for i in range (1, max_number+1):
    if i % 3 == 0 and i % 5 == 0:
        print(x)
    elif i % 3 == 0:
        print(y)
    elif i % 5 == 0:
        print(z)
    else:
        print(i)
