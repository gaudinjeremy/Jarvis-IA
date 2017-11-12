#!/usr/bin/python

import sys
import time
from lxml import etree

tree = etree.parse("./plugins_installed/Jarvis-IA/api/brain.xml")

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

def AddTest():
	for user in tree.xpath("/users/user"):
    	print(user.get("data-id"))

def main():
	global TOSAY

	if sys.argv[1] == "test1":
		test1(sys.argv[2])
	elif sys.argv[1] == "test2":
		test2(sys.argv[2])
	elif sys.argv[1] == "tree":
		AddTest()
	else:
		TOSAY = "Commande inconnue"

	print TOSAY

if __name__ == "__main__":
	main()
