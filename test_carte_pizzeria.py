from carte_pizzeria import CartePizzeria
from unittest.mock import Mock
from pizza import Pizza

def test_has_no_pizzas():
    carte_pizzeria = CartePizzeria([])
    assert carte_pizzeria.is_empty() == True
    assert carte_pizzeria.nb_pizzas() == 0

def test_has_pizza():
    # Setup
    pizza = Mock(spec=Pizza)

    # Exercice
    carte_pizzeria = CartePizzeria(pizza)
    
    # Assert
    assert carte_pizzeria.is_empty() == False
    assert carte_pizzeria.nb_pizzas() == 1

def test_can_add_pizza():
    # Setup
    pizza = Mock(spec=Pizza)

    # Exercice
    carte_pizzeria = CartePizzeria([])
    carte_pizzeria.add_pizza(pizza)

    # Assert
    assert carte_pizzeria.is_empty() == False
    assert carte_pizzeria.nb_pizzas() == 1

def test_can_remove_pizza():
    # Setup
    pizza = Mock(spec=Pizza)
    pizza.nom = "chevre"
    
    # Exercice
    carte_pizzeria = CartePizzeria(pizza)
    carte_pizzeria.remove_pizza("chevre")

    # Assert
    assert carte_pizzeria.is_empty() == True
    assert carte_pizzeria.nb_pizzas() == 0