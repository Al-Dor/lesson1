def cut_cake(parts):
	try:
		return 1 / int(parts)
	except (ZeroDivisionError, TypeError, ValueError):
		return 'С ума посходили?'

cake = cut_cake('я вас любил')
print(cake)