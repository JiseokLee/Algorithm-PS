n, m = map(int, input().split())
mat1 = []
mat2 = []

for _ in range(n): mat1.append(list(map(int, input().split())))
for _ in range(n): mat2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m): print(mat1[i][j] + mat2[i][j], end=' ')
    print()
