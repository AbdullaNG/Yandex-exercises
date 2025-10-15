txt = input()
l = [
    [" * ", "* *", "***", "* *", "* *"],
    ["** ", "* *", "** ", "* *", "** "],
    [" * ", "* *", "*  ", "* *", " * "]
]
out = ["", "", "", "", ""]

for z in txt:
    x = ord(z) - ord('A')
    letter = l[x]
    for i in range(5):
        if out[i]:
            out[i] += "  "
        out[i] += letter[i]

for j in out:
    print(j)