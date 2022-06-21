word = input()
mostFreqCnt = 0
freq = {}
mostFreq = []

for ch in word:
    if (ch.upper() in freq): freq[ch.upper()] += 1
    else: freq[ch.upper()] = 1

for key in freq:
    if (freq[key] > mostFreqCnt): mostFreqCnt = freq[key]

for key in freq:
    if (freq[key] == mostFreqCnt): mostFreq.append(key)

if (len(mostFreq) > 1): print('?')
else: print(mostFreq[0])