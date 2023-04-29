assinatura = input("Informe aqui o seu tipo de assinatura")
faturamento = float(input("Informe agora o valor do seu faturamento"))
porcentagem = float

if assinatura == "Basic":
    porcentagem = faturamento * 0.3
elif assinatura == "Silver":
    porcentagem = faturamento * 0.2
elif assinatura == "Gold":
    porcentagem = faturamento * 0.1
elif assinatura == "Platinum":
    porcentagem = faturamento * 0.05


print("Seu bonus a pagar é de R${}".format(porcentagem))
