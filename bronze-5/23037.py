n = int(input())
result = 0

for i in range(4, -1, -1):
    result += (n // (10 ** i)) ** 5
    n = n % (10 ** i)

print(result)