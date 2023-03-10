qtd_rodas = int(input("Digite aqui a quantidade de rodas: "))
tripulantes = int(input("Digite aqui a quantidade de tripulantes no veículo: "))
peso = int(input("Digite aqui o peso em KG: "))



if (2 <= qtd_rodas <= 3):
    print("Sua categoria é 'A' ")
elif (qtd_rodas == 4 and tripulantes <= 8 and peso < 3500):
    print("Sua categoria é 'B' ")
elif (qtd_rodas >= 4 and 3500 <= peso <= 6000):
    print("Sua categoria é 'C' ")
elif (qtd_rodas >= 4 and tripulantes > 8):
    print("Sua categoria é 'D' ")
elif (qtd_rodas >= 4 and peso > 6000):
    print("Sua categoria é 'D'")
else:
    print("Ocorreu algum erro, tente novamente !!")

print(tripulantes)