word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for ch in alphabet:
    pos = -1
    for i in range(0, len(word)):
        if (word[i] == ch):
            pos = i
            break
    print(pos, end=' ')
    