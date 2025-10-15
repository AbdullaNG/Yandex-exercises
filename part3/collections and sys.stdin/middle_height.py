import sys
 
 
s = 0
c = 0

for i in sys.stdin:
    s += int(i)
    c += 1

if c > 0:
    print(s / c)
else:
    print(-1)