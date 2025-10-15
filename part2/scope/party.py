people = {}
 
 
def add_friends(name_of_person, list_of_friends):
	x = people.get(name_of_person)
	if x:
		people[name_of_person] = x + list_of_friends
	else:
		people[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
	if name_of_person2 in people[name_of_person1]:
		return True
	return False


def print_friends(name_of_person):
	s = reversed(people[name_of_person])
	for i in s:
		print(i, end=' ')
	print()



add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))