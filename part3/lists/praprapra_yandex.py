n = int(input())
listt = []
for i in range(n):
    txt = input()
    listt.append(txt)
search = input()
for j in listt:
    if search in j:
        print(j)