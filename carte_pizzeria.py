from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    def __init__(self, pizzas: list[Pizza]):
        self.pizzas = []
        if isinstance(pizzas, Pizza):
            self.pizzas.append(pizzas)
        else:
            for pizza in pizzas:
                self.pizzas.append(pizza)

    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name: str):
        try:
            for pizza in self.pizzas:
                if pizza.nom == name:
                    self.pizzas.remove(pizza)
                    return
            raise CartePizzeriaException
        except CartePizzeriaException:
            print(f"La pizza '{name}' n'existe pas!")

        