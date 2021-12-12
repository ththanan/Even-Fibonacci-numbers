# Problem 2

a = 1
b = 2
all_even = 2
while b < 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        all_even += c
print(all_even)