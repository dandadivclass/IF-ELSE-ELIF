print("Quer saber quanto seu patinete percorreu aqui pelo bairro?")

distancia = float(input("Qual foi a distância que você percorreu?"))
tempo = float(input("Em quanto tempo você percorreu essa distância?"))
velocidade = distancia / tempo

print("A velocidade percorrida por você e seu patinete foi de {0:.2f} m/min" .format(velocidade))
