n = int(input())
count = 0
x = 0

for i in range(n):
    txt = input()
    count += 1
    x = 0
    if 'кот' in txt:
        for j in txt:
            if j == 'к' and txt[x + 1] == 'о':
                print(count, x + 1)
            else:
                x += 1
    else:
        continue