class Drinks:
    kind = "Drink"
    def __init__(self,name):
       self.name=name
um = Drinks("laranja")
dois = Drinks("coca-cola")
tres = Drinks("mineral")
print(um.kind)
print(um.name)
