#!/usr/bin/python

import sys

TOSAY=""

def test1(arg):
	global TOSAY

	try:
		TOSAY = arg

	except  Exception as e:
		TOSAY = "erreur fonction 1"

	return TOSAY

def test2(arg):
	global TOSAY

	try:
		TOSAY = arg

	except  Exception as e:
		TOSAY = "erreur fonction 2"

	return TOSAY

def main():
	global TOSAY

	if sys.argv[1] == "test1":
#		test1(sys.argv[2])
		TOSAY = "echo de test 1"
	elif sys.argv[1] == "test2":
#		test2(sys.argv[2])
		TOSAY = "echo de test 2"
	else:
		TOSAY = "Commande inconnue"

	print TOSAY

if __name__ == "__main__":
	main()
