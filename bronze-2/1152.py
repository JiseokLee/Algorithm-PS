string = input()
cnt = 0

if (string == ' '): cnt = 0
else:
    for i in range(len(string)):
        if (string[i] == ' ' and i != 0 and i != len(string) - 1):
            cnt += 1
    cnt += 1

print(cnt)