def array_diff(a,b):
	for el in b:
		while a.count(el)!=0:
			a.pop(a.index(el))
	return a