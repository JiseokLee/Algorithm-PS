n, x = map(int, input().split())
mat = list(map(int, input().split()))

for i in mat:
    if (i < x): print(i, end=' ')