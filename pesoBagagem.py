peso_bag = float(input("Informe o peso da sua bagagem:"))
input("Qual o seu tipo-cliente?")
tipo_cliente = str("Premium")
tipo_cliente2 = str("Popular")

if peso_bag <= 34 and tipo_cliente == "Premium":
    print("Peso permitido para cliente Premium")

elif peso_bag > 28 and tipo_cliente2 == "Popular":
    print("Peso acima do permitido!")

else:
    print("Peso permitido para clientes")
