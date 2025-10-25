# implementar 3 operações: depósito, saque e extrato.
# todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
# caso o usuário não tenha saldo em conta deve ser exibido uma mensagem informa que não é possível sacar.
# até 3 saques diários com limite máximo de 500 reais por saque.

# operação extrato:
# essa operação deve exibir todos os depósitos e saques feitos na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# os valores devem ser exibidos utilizando o formato float R$: xxx.xx

import os


def limpar_tela():
    os.system("cls")


menu = """
Bem vindo(a) ao JonBank!
Selecione a opção desejada:

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    limpar_tela()
    opcao = input(menu).upper()

    if opcao == "D":
        limpar_tela()
        while True:
            try:
                valor = float(input("Digite o valor a ser depositado: "))
                if valor > 0:
                    saldo += valor
                    extrato.append(valor)
                    break
                else:
                    input("Valor inválido, pressione enter para continuar...")
            except ValueError:
                input("O valor deve ser numérico!")

    elif opcao == "S":
        limpar_tela()
        while True:
            try:
                valor = float(input("Digite o valor a ser sacado:"))
                if valor > 0:
                    if numero_saques < LIMITE_SAQUES:
                        if saldo >= valor:
                            saldo -= valor
                            numero_saques += 1
                            extrato.append(valor)
                            break
                        else:
                            input(
                                "Saldo insuficiente para o saque, pressione enter para continuar..."
                            )
                    else:
                        print(
                            "Valor máximo de saques diários atingido, tente novamente mais tarde!"
                        )
                        input()
                        break
                else:
                    input("Valor inválido, pressione enter para continuar...")
            except ValueError:
                input("O valor deve ser numérico!")

    elif opcao == "E":
        limpar_tela()
        print(f"Saldo em conta: {saldo:.2f}")
        print(f"Extrato: {extrato}")
        input("\nPressione enter para voltar ao menu...")

    elif opcao == "Q":
        limpar_tela()
        print("saindo do sistema...")
        break

    else:
        limpar_tela()
        input("Opção inválida, pressione enter para continuar...")
