x = set()
y = set()
count = 0

n = int(input())
for i in range(n):
    name = input()
    if name in x:
        y.add(name)
        count += 1
    else:
        x.add(name)

count += len(y)
print(count)