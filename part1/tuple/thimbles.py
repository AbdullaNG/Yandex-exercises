n = int(input())
lt = [''] * n

for i in range(n):
    lt[i] = input()
    
k = int(input())

for i in range(k):
    x = int(input())
    tl = [''] * x
    for j in range(x):
        tl[j] = lt[int(input()) - 1]
    lt = tl
    
for i in range(len(lt)):
    print(lt[i])