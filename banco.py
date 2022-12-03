from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('================================')
    print('============= ATH ==============')
    print('================================')

    print('Selecione uma opção no menu: ')
    print('1- Criar conta')
    print('2- Efetuar saque')
    print('3- Efetuar depósito')
    print('4- Efetuar transferência')
    print('5- Listar contas')
    print('6- sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('volte sempre! ')
        sleep(2)
        exit(0)
    else:
        print('opção inválida. ')
        sleep(2)
        menu()

def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = validar_cpf('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso. ')
    print('Dados da conta: ')
    print('-----------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if not contas:
        print('ainda não existem contas cadastradas. ')
        sleep(2)
        menu()
    else:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero()

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}. ')
    sleep(2)
    menu()

def efetuar_deposito() -> None:
    if not contas:
        print('Ainda não existem contas cadastradas. ')
        sleep(2)
        menu()
    else:
        numero: int = int(input('Informe o numero da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor do depósito: "))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com o número {numero}')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if not contas:
        print('Ainda não existem contas cadastradas. ')
    else:
        numero_origem: int = int(input('Informe o número da sua conta: '))

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Informe o número da conta destino: '))

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta com número {numero_destino} não foi encontrada. ')
        else:
            print(f'A sua conta com número {numero_origem} não foi encontrada. ')



def listar_contas() -> None:
    if not contas:
        print('Não existem contas cadastradas. ')
    else:
        print('Listagem de contas: ')

        for conta in contas:
            print(conta)
            print('------------------')
            sleep()
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    if contas:
        for conta in contas:
            if conta.numero == numero:
                return conta


if __name__ == '__main__':
    main()