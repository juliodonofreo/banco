import datetime
from typing import List
from time import sleep
from datetime import date

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def validar_nome(texto = '') -> str:
    while True:
        # Converte a primeira letra do nome para maiúscula
        nome: str = str(input(texto)).capitalize()
        # Caso a entrada digitada esteja vazia
        if nome == '':
            print('O nome não pode ficar vazio. ', end='')
        # Caso a entrada digitada não contenha apenas letras
        elif not nome.replace(' ', '').isalpha():
            print('O nome deve conter apenas letras. ', end='')
            sleep(1)
        # Caso a entrada digitada contenha menos que dois caracteres
        elif len(nome) < 2:
            print('O nome precisa ter ao menos duas letras. ', end='')
            sleep(1)
        else:
            return nome


def validar_cpf(texto = '') -> str:
    while True:
        cpf: str = str(input(texto)).replace('.', '').replace('-', '').strip()
        if cpf.isnumeric():

            if len(cpf) != 11:
                print('o cpf deve ter exatamente 11 dígitos, digite novamente. ', end='')
            else:
                soma = sum((int(digito) * i for digito, i in zip(cpf, range(10, 1, -1))))
                primeiro_validador = 11 - (soma%11)
                soma = sum((int(digito) * i for digito, i in zip(cpf, range(11, 1, -1))))
                segundo_validador = 11 - (soma%11)

                if primeiro_validador >= 10:
                    primeiro_validador = 0
                if segundo_validador >= 10:
                    segundo_validador = 0

                if str(primeiro_validador) == cpf[-2] and str(segundo_validador) == cpf[-1]:
                    return cpf
                else:
                    print('cpf inválido, digite novamente. ', end='')
        else:
            print('o cpf deve ser um número. ', end='')


def validar_email(texto = '') -> str:
    while True:
        try:
            email: str = input(texto).lower()
            local, dominio = email.split('@')[0], email.split('@')[1]
        except IndexError:
            print('email inválido. ', end='')
        else:
            if email[-1:-5:-1] != 'moc.':
                print('o email deve terminar com ".com" ', end='')
            elif len(local) > 64:
                print('a primeira parte do email pode ter no máximo 64 caracteres. ', end='')
            elif len(dominio) > 63:
                print('o dominio deve ter no maximo 63 caracteres. ', end='')
            elif not dominio.replace('.', '').isalnum():
                print('O dominio só pode possuir numeros ou letras. ', end='')
            else:
                return email



def validar_data(texto = '') -> str:
    while True:
        data: str = input(texto).replace('-', '/').replace('.', '/')
        dia: str = data.split('/')[0]
        mes: str = data.split('/')[1]
        ano: str = data.split('/')[2]
        ano_atual = datetime.datetime.now().year
        if not data.replace('/', '').isnumeric() or len(data) != 10:
            print('por favor insira uma data válida. ', end='')
        elif int(dia) > 31 or int(dia) < 0:
            print('dia inválido.')
            sleep(2)
        elif int(mes) > 12 or int(mes) <= 0:
            print('mes invalido. ')
            sleep(2)
        elif int(ano) > ano_atual - 18:
            print('Cliente com idade inválida. ')
            sleep(2)
        elif len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
            print('formato de data inválido. ')
        else:
            return data


def validar_int(texto = '') -> int:
    while True:
        try:
            num: int = int(input(texto))
        except ValueError:
            print('o valor deve ser um número inteiro. ', end='')
            validar_int(texto)
        else:
            return num


def validar_float(texto = '') -> float:
    while True:
        try:
            num: float = float(input(texto))
        except ValueError:
            print('o valor deve ser um número. ', end='')
        else:
            return num


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

    opcao: int = validar_int()

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

    nome: str = validar_nome('Nome do cliente: ')
    email: str = validar_email('E-mail do cliente: ')
    cpf: str = validar_cpf('CPF do cliente: ')
    data_nascimento: str = validar_data('Data de nascimento do cliente: ')

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
        numero: int = validar_int('Informe o número da sua conta: ')

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = validar_float('Informe o valor do saque: ')

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
        numero: int = validar_int('Informe o numero da sua conta: ')

        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = validar_float("Informe o valor do depósito: ")

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
                valor: float = validar_float('Informe o valor da transferência: ')

                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta com número {numero_destino} não foi encontrada. ')
                sleep(2)
                menu()
        else:
            print(f'A sua conta com número {numero_origem} não foi encontrada. ')
            sleep(2)
            menu()


def listar_contas() -> None:
    if not contas:
        print('Não existem contas cadastradas. ')
        sleep(2)
    else:
        print('Listagem de contas: ')

        for conta in contas:
            print(conta)
            print('------------------')
            sleep(2)
    menu()


def buscar_conta_por_numero(numero: int, /) -> Conta:
    if contas:
        for conta in contas:
            if conta.numero == numero:
                return conta


if __name__ == '__main__':
    main()