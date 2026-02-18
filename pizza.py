class Pizza:
    def __init__(self, nom: str, ingredients: list[str], prix: float):
        self.nom = nom
        self.prix = prix
        self.ingredients = []
        for item in ingredients:
            self.ingredients.append(item)