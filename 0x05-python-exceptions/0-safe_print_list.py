#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
	'''function that prints x elements of a list'''
	index = 0

	try:
		while index < x:
			print("{}".format(my_list[index]), end="")
			index += 1

	except IndexError:
		pass

	print()
	return index
