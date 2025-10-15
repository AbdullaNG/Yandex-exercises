types = {
	type(5): 'int',
	type('a'): 'str',
	type(3.5): 'float',
	type([]): 'list',
	type({}): 'dict',
	type(set()): 'set',
	type(True): 'bool',
	type(()): 'tuple'
}

int_t = []
str_t = []
float_t = []
list_t = []
dict_t = []
set_t = []
bool_t = []
tuple_t = []
newlt = []
d = {}


def typification(lt):
	for i in lt:
		if types[type(i)] == 'int':
			int_t.append(i)
		elif types[type(i)] == 'str':
			str_t.append(i)
		elif types[type(i)] == 'float':
			float_t.append(i)
		elif types[type(i)] == 'list':
			list_t.append(i)
		elif types[type(i)] == 'dict':
			dict_t.append(i)
		elif types[type(i)] == 'set':
			set_t.append(i)
		elif types[type(i)] == 'bool':
			bool_t.append(i)
		elif types[type(i)] == 'tuple':
			tuple_t.append(i)
	if int_t != []:
		d['int'] = int_t
	if str_t != []:
		d['str'] = str_t
	if float_t != []:
		d['float'] = float_t
	if list_t != []:
		d['list'] = list_t
	if dict_t != []:
		d['dict'] = dict_t
	if set_t != []:
		d['set'] = set_t
	if bool_t != []:
		d['bool'] = bool_t
	if tuple_t != []:
		d['tuple'] = tuple_t
	return d