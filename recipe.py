class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare ")

pizza = Recipe("Pizza", ["cheese", "bread", "tomoato"], 45)
pasta = Recipe("Pizza", ["penne", "sauce", ], 55)pwd


print(pizza.items)
print(pasta.items)

print(pizza.contents())

