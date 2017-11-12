#!/usr/bin/python

import sys
import time
from lxml import etree

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

	tree = etree.parse("./plugins_installed/Jarvis-IA/api/Brain.xml")
	for user in tree.xpath("/plugins/plugin[nom='micro']/value"):
		print user.text

def AddCell():

	tree = etree.parse("./plugins_installed/Jarvis-IA/api/Brain.xml")
	plugins = etree.Element("plugins")
	plugin = etree.SubElement(plugins, "plugin")
	plugin.set("data-id", "103")
	nom = etree.SubElement(plugin, "test")
	nom.text = "Zorro"
	value = etree.SubElement(plugin, "value")
	value.text = "Danseur"
	tree.write('./plugins_installed/Jarvis-IA/api/Brain2.xml')

def main():
	global TOSAY

	if sys.argv[1] == "test1":
		test1(sys.argv[2])
	elif sys.argv[1] == "test2":
		test2(sys.argv[2])
	elif sys.argv[1] == "tree":
		AddTest()
	elif sys.argv[1] == "cell":
		AddCell()
	else:
		TOSAY = "Commande inconnue"

	print TOSAY

if __name__ == "__main__":
	main()
