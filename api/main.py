#!/usr/bin/python

import sys
import random
import time
import pickle

TOSAY = ""


# renvoi le contenu du "BRAIN" de Jarvis
def getJarvisBrain():
	global TOSAY

	with open('Brain.jarvis', 'rb') as fichier:
		jarvisBrain = pickle.Unpickler(fichier)
		brain = jarvisBrain.load()

	TOSAY = brain
	return brain

# modifie le contenu du "BRAIN" de Jarvis
def updateJarvisBrain(brain):

	with open('Brain.jarvis', 'wb') as fichier:
		jarvisBrain = pickle.Pickler(fichier)
		jarvisBrain.dump(brain)

	getValue("IA", "confirmation")


# crée le "BRAIN" de Jarvis
def initIA():
	global TOSAY

	brain = {}
	brain['IA'] = {
	"confirmation" : ["voila", "c'est fait"],
	"erreur" : ["aie", "oupss"],
	}

	updateJarvisBrain(brain)


# Permet d'ajouter un plugin et ses clefs au "BRAIN" de Jarvis
def initPlugin(plugin, key):
	global TOSAY

	brain = getJarvisBrain()

	if brain.has_key(plugin):
		jarvis = brain.get(plugin)

		if jarvis.has_key(key):
			#updateValue(plugin, key, value)

		else:
			addKey(plugin, key)

	else:
		addPlugin(plugin)
		initPlugin(plugin, key)


# renvoi une valeur appartenant au plugin et à la clef envoyé
def getValue(plugin, key):
	global TOSAY

	brain = getJarvisBrain()

	if brain.has_key(plugin):
		jarvis = brain.get(plugin)

		if jarvis.has_key(key):
			value = jarvis.get(key)

			if isinstance(value, list):
				TOSAY = random.choice(value)
			else:
				TOSAY = value
		else:
			TOSAY = "clef introuvable"
	else:
		TOSAY = "Plugin introuvable"


# Ajoute un plugin au "BRAIN" de Jarvis
def addPlugin(plugin):
	global TOSAY

	brain = getJarvisBrain()

	if brain.has_key(plugin):
		TOSAY = "ce plugin existe deja"

	else:
		brain[plugin] = {}
		updateJarvisBrain(brain)


# Ajoute une clefs au plugins envoyé au "BRAIN" de Jarvis
def addKey(plugin,key):
	global TOSAY

	brain = getJarvisBrain()

	if brain.has_key(plugin):
		jarvis = brain.get(plugin)

		if jarvis.has_key(key):
			TOSAY = "cette clef existe deja"

		else:
			brain[plugin] = {
			key : ["0"],
			}

			updateJarvisBrain(brain)

	else:
		TOSAY = "ce plugin n'existe pas"


# Ajoute une valeur au plugins et à la clef envoyé au "BRAIN" de Jarvis
def addValue(plugin,key,value):
	global TOSAY

	brain = getJarvisBrain()

	if brain.has_key(plugin):
		jarvis = brain.get(plugin)

		if jarvis.has_key(key):

			newValue = jarvis.get(key)
			newValue.append(value)

			brain[plugin] = {
			key : newValue,
			}

			updateJarvisBrain(brain)

		else:
			TOSAY = "Cette clef n'existe pas"
	else:
		TOSAY = "ce plugin n'existe pas"


# modifie une valeur au plugins et à la clef envoyé au "BRAIN" de Jarvis
def updateValue(plugin,key,value):
	global TOSAY

	brain = getJarvisBrain()

	if brain.has_key(plugin):
		jarvis = brain.get(plugin)

		if jarvis.has_key(key):

			brain[plugin] = {
			key : [value],
			}

			updateJarvisBrain(brain)

		else:
			TOSAY = "Cette clef n'existe pas"
	else:
		TOSAY = "ce plugin n'existe pas"


def main():
	global TOSAY

	if sys.argv[1] == "initIA":
		initIA()

	elif sys.argv[1] == "initPlugin":
		initPlugin(sys.argv[2], sys.argv[3])

	elif sys.argv[1] == "getBrain":
		getJarvisBrain()

	elif sys.argv[1] == "addPlugin":
		addPlugin(sys.argv[2])

	elif sys.argv[1] == "addKey":
		addKey(sys.argv[2], sys.argv[3])

	elif sys.argv[1] == "addValue":
		addValue(sys.argv[2], sys.argv[3], sys.argv[4])

	elif sys.argv[1] == "updateValue":
		updateValue(sys.argv[2], sys.argv[3], sys.argv[4])

	elif sys.argv[1] == "getValue":
		getValue(sys.argv[2], sys.argv[3])

	else:
		TOSAY = "Commande inconnue dans mon IA"

	print TOSAY

if __name__ == "__main__":
	main()
