col = int(input())
row = int(input())
table = []
temp = []

for i in range(col):
    temp = []
    for x in range(row):
        temp.append(input())
    table.append(temp)

for j in table:
    for x in j:
        print(x, end="\t")
    print()