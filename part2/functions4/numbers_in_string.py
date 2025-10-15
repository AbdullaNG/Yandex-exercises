def from_string_to_list(string, container):
	container.extend([int(i) for i in string.split()])