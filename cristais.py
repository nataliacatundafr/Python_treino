plantas = int( input( "Qual semente você quer comprar?\n"
                      "1:Comigo-ninguém-pode"
                      "\n2:Roseira"
                      "\n3:Abacaxi"
                      "\n4:Banana"))
lista_plantas=["Comigo-ninguém-pode","Roseira","Abacaxi","Banana"]
lista_aleatoria=["Giboia","Pitanga"]
if plantas == 1:
    print("Comigo-ninguém-pode" )
else:
    if plantas == 2:
        print("Roseira")
    else:
        if plantas == 3:
            print( "Abacaxi" )
        else:
            if plantas == 4:
                print("Banana")
            else:
                if plantas > 4:
                    print("podemos escolher duas para você!")
                    for f in sorted(set(lista_aleatoria)):
                        print(f)
adicione = input("Adicione um desejo de semente que quer: ")
print(adicione)
