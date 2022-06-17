total_apples = int(input())
more_apples = int(input())

if (total_apples % 2 == 0):
    print(total_apples // 2 + more_apples // 2)
    print(total_apples // 2 - more_apples // 2)
else:
    print(total_apples // 2 + more_apples // 2 + 1)
    print(total_apples // 2 - more_apples // 2)