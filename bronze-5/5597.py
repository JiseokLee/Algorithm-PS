students = []
for i in range(1, 31): students.append(i)
for _ in range(28): students.remove(int(input()))
print(students[0])
print(students[1])