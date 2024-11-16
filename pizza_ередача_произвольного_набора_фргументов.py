def make_pizza(*topings):
	"""Ввод списка заказанных топингов"""
	print(topings)

make_pizza('pepperoni')
make_pizza('pepperoni', 'hamster')

def make_pizza(*topings):
	"""Выводит описание пиццы"""
	print("\nМайк твоя сука пица самая крутая мазафакерс:")
	for toping in topings:
		print(f"- {toping}")

make_pizza('pepperoni')
make_pizza('pepperoni', 'hamster')