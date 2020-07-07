class Drinks:
    kind = "Drink"
    def __init__(self,name):
       self.name=name
one = Drinks("Orange juice")
two = Drinks("coca-cola")
three = Drinks("water")
print(two.kind)
print(two.name)
