set1 = set()
set2 = set()
set3 = set()
flag = True
num = input()

while num:
    if num == "-1":
        if flag:
            set1 = set3
            flag = False
        else:
            set2 = set2.union(set1.intersection(set3))
            seta = set1.symmetric_difference(set3)
            set1 = seta.difference(set2)
        set3 = set()
    else:
        set3.add(num)
    num = input()

for i in set1:
	print(i, end=' ')