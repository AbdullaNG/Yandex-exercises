t1 = input()
t2 = input()
bull = 0
cow = 0

for i in range(len(t1)):
    if t1[i] == t2[i]:
        bull += 1
    for j in range(len(t1)):
        if t1[i] == t2[j] and i != j:
            cow += 1
print(bull, cow)
