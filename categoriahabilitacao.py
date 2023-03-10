# Desenvolva um código que utilize as seguintes características de um veículo:
# - Quantidade de rodas;
# - Peso bruto em quilogramas;
# - Quantidade de pessoas no veículo.

# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

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
