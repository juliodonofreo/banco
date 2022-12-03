from models.cliente import Cliente
from models.conta import Conta

gabs: Cliente = Cliente('gabriel', 'gabsbotadinha@yahoo.com', '123.456.789-01', '03/12/1999')
julio: Cliente = Cliente('Julio', 'julio.bibico@hotmail.com', '987.654.321-00', '25/05/2001')

conta1: Conta = Conta(gabs)
conta2: Conta = Conta(julio)

print(gabs)
print(julio)
print(conta1)
print(conta2)