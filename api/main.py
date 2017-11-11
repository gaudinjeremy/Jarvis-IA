#!/usr/bin/python

import sys

TOSAY=""

def test1(arg=""):
	global TOSAY
	try:
		TOSAY = arg

	except  Exception as e:
		TOSAY = "erreur fonction 1"

	return TOSAY

def test2(arg=""):
	global TOSAY
	try:
		TOSAY = arg

	except  Exception as e:
		TOSAY = "erreur fonction 2"

	return TOSAY

def router(arg):
	return {
		'test1': test1,
		'test2': test2
	}

def main():
	global TOSAY
	routes = router(sys.argv)
	try:
		routes[sys.argv[2]]
	except  Exception as e:
		print str(e)
		TOSAY = "erreur"

	print TOSAY

if __name__ == "__main__":
	main()
