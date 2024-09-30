#!/usr/bin/python3

'''function that prints x elements of a list'''

def safe_print_list(my_list=[], x=0):
	index = 0
	try:
		while index < x:
			print("{}".format(my_list[index]), end="")
			index += 1
	except IndexError:
		pass

	print()
	return index
