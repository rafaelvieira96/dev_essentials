#!/usr/bin/python3


class Conta():
    '''Tentando abstrair uma conta'''

    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
                
    def sacar(self, valor):
        self.saldo -= valor
            
    def depositar(self, valor):
        self.saldo += valor
        
    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)

        
c1 = Conta('daniel', 232323, 1500)
c2 = Conta('rafael', 1212122, 2000)
c1.sacar(500)
print(c1.saldo, c1.titular, sep='\n')