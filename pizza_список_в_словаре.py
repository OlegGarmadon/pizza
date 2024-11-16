# Сохранение информации о заказанной пицце.

pizza = {
	'crust': 'thick',
	'toppings': ['грибы', 'экстра сыр'],
	}

# Описание заказа.
print(f"You ordered a {pizza['crust']}-crst pizza"
	" Wiht the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'rudi'],
    'sarah': ['c', 'python'],
    'edward': ['rudi','java'],
    'phil': ['python', 'c++'],
}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}") 