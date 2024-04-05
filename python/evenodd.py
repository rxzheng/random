n = int(input("write your n: "))
if n % 2 == 1:
    n = 5 - 2 * n
    print(n)
if n % 2 == 0:
    n = n**2 + 1
    print(n)
