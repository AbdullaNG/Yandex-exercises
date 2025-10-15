txt = input().lower()
word = [txt.count(i) for i in txt]
print(max(word))