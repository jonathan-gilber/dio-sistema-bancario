# implementar 3 operações: depósito, saque e extrato.
# todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
# caso o usuário não tenha saldo em conta deve ser exibido uma mensagem informa que não é possível sacar.
# até 3 saques diários com limite máximo de 500 reais por saque.

# operação extrato:
# essa operação deve exibir todos os depósitos e saques feitos na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# os valores devem ser exibidos utilizando o formato float R$: xxx.xx

import os
from rich import print
from datetime import datetime


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
                valor = float(input("Digite o valor a ser depositado: R$ "))
                if valor > 0:
                    saldo += valor
                    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    extrato.append(f"[dim]{hora}[/dim] [green]+ R$ {valor:.2f}[/green]")
                    print(f"\nDepósito concluído! Saldo atual: R$ {saldo:.2f}")
                    input("Pressione Enter para continuar...")
                    break
                else:
                    input("Valor inválido, pressione Enter para continuar...")
            except ValueError:
                input("O valor deve ser numérico! Pressione Enter para continuar...")

    elif opcao == "S":
        limpar_tela()
        while True:
            try:
                valor = float(input("Digite o valor a ser sacado: R$ "))
                if valor > 0:
                    if numero_saques < LIMITE_SAQUES:
                        if saldo >= valor:
                            if valor <= limite:
                                saldo -= valor
                                numero_saques += 1
                                hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                extrato.append(f"[dim]{hora}[/dim] [red]- R$ {valor:.2f}[/red]")
                                print(f"\nSaque concluído! Saldo atual: R$ {saldo:.2f}")
                                input("Pressione Enter para continuar...")
                                break
                            else:
                                input("Limite máximo por saque é R$ 500. Pressione Enter para continuar...")
                        else:
                            input("Saldo insuficiente para o saque. Pressione Enter para continuar...")
                    else:
                        print("Limite diário de saques atingido! Tente novamente amanhã.")
                        input()
                        break
                else:
                    input("Valor inválido, pressione Enter para continuar...")
            except ValueError:
                input("O valor deve ser numérico! Pressione Enter para continuar...")

    elif opcao == "E":
        limpar_tela()
        print("\n[bold white]EXTRATO BANCÁRIO[/bold white]\n")
        if extrato:
            for item in extrato:
                print(item)
        else:
            print("[dim]Nenhuma movimentação registrada.[/dim]")
        print(f"\n[bold white]Saldo em conta: R$ [/bold white]{saldo:.2f}")
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "Q":
        limpar_tela()
        if input("Deseja realmente sair? (S/N): ").upper() == "S":
            break

    else:
        limpar_tela()
        input("Opção inválida, pressione Enter para continuar...")