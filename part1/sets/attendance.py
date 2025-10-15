m = int(input())
students = set()

for x in range(int(input())):
    b = input()
    students.add(b)

for y in range(m - 1):
    all = set()
    for z in range(int(input())):
        a = input()
        all.add(a)
    students = students.intersection(all)

for student in students:
    print(student)