n = int(input())
n_list = []
cnt = 0

n_list = list(map(int, input().split()))
target_n = int(input())

for i in n_list:
    if (i == target_n): cnt += 1

print(cnt)