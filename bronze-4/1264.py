vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input().lower()
    if (s == '#'): break

    cnt = 0
    for ch in s:
        if (ch in vowels): cnt += 1
    print(cnt)