a = float(input("input a"))

while a**2 > (a + 0.01) or a ** 2 < (a - 0.01):
    a = 0.5 * (a + (2 / a))
    print(a)
print(a)
