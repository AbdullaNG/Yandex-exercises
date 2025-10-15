n = int(input())
clients = []

for i in range(n):
	client = int(input())
	clients.append(client)

for j in clients:
	print(j)
print()
for x in clients:
	print(x * 3)