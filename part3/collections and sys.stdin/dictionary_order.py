txt = input().split()
print(' '.join(sorted(txt, key=lambda x: x.lower())))