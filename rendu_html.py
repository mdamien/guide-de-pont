import json

categories = json.load(open('commerces.json'))

print('<pre>')
for categorie, commerces in categories.items():
	print('<h1>', categorie, '</h1>', sep='')
	for commerce in commerces:
		for attribut, valeur in commerce.items():
			print(attribut, ':', valeur)
		print()
	print()