menu = """
       [1] Depositar
       [2] Sacar
       [3] Extrato
       [0] Sair

       =>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        opcao = int(input("[1] Cancelar \n[2] Continuar \n"))

        if opcao == 1:
            print("Operação cancelada!")
        elif opcao == 2:
           
            valor = float(input("Infome o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operaçõa inválida, por favor selecionar navamente a operação desejada.")
        else:
            print("Operaçõa inválida, por favor selecionar navamente a operação desejada.")

    elif opcao == "2":
        opcao = int(input("[1] Cancelar \n[2] Continuar \n"))

        if opcao == 1:
            print("Operação cancelada!")
        elif opcao == 2:
            valor = float(input("Infome o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUE

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo sufuciente.")

            elif excedeu_limite:
                print("Operaçõa falhou! O valor do saque excedeu o limete.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Operaçõa inválida, por favor selecionar navamente a operação desejada.")


    elif opcao == "3":
        print("\n==========// EXTRATO //============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "9":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
