class Person:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

n = Person("Natália Catunda Freitas","27 anos")
p = Person("Paulo Andrande Nascimento","28 anos")
print(p.nome, p.idade)