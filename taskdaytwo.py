print("Bem-vindo ao calculador de pagamento!")
conta = float(input("Diga, qual o total da conta?\n$"))
gorjeta = int(input("Qual a porcentagem da gorjeta?\nColoque apenas o valor, sem o simbolo %\n"))
pessoas = int(input("Em quantos será divido a conta?\n"))

conta = ((((gorjeta / 100) * conta) + conta) / pessoas)

print(f"\nO total do valor pago pro pessoa é: ${conta}")

