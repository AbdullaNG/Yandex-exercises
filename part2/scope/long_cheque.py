cheque = 1
items = 0
s = 0
lt = []


def add_item(item_name, item_cost):
	global cheque
	global items
	global s
	global lt
	items += 1
	s += item_cost
	lt.append(f'{item_name} - {item_cost}')


def print_receipt():
	global lt
	global cheque
	global items
	global s
	if lt != []:
		print(f'Чек {cheque}. Всего предметов: {items}')
		for i in lt:
			print(i)
		print(f'Итого: {s}')
		print('-----')
		cheque += 1
	
	items = 0
	s = 0
	lt = []