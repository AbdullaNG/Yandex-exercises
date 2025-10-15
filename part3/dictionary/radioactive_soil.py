p = input().split()
txt = input().split()
rads = input().split()
m = float(input())
rads = [float(a) for a in rads]
final = []
d = {}
newd = {}
z = 0

for i in range(0, len(p), 2):
    tp = p[i]
    x = int(p[i + 1])
    d[tp] = x

for i in range(len(txt)):
    tp = txt[i]
    if tp not in newd:
        newd[tp] = []
    newd[tp].append(rads[i])
total = sum(rads)

while total > m:
    z += 1
    total = 0

    for tp in newd:
        x = d[tp]
        newlt = []

        for j in newd[tp]:
            new_rads = j * 0.5 ** (z / x)
            newlt.append(new_rads)

        newd[tp] = newlt
        total += sum(newlt)

for i in range(len(txt)):
    tp = txt[i]
    final.append(newd[tp].pop(0))

print(z)
print(" ".join(str(a) for a in final))