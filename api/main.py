#!/usr/bin/python

import sys
import time
from lxml import etree

tree = etree.parse("./jarvis/plugins_installed/Jarvis-IA/api/brain.xml")

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
	users = etree.Element("users")
	user = etree.SubElement(users, "user")
	user.set("data-id", "101")
	nom = etree.SubElement(user, "nom")
	nom.text = "Zorro"
	metier = etree.SubElement(user, "metier")
	metier.text = "Danseur"
	print(etree.tostring(users, pretty_print=True))

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
