n = int(input())
a = 0
b = 1
c = 1

if (n == 0): print(0)
elif (n == 1 or n == 2): print(1)
else:
    for _ in range(n - 2):
        a = b
        b = c
        c = a + b
    print(c)