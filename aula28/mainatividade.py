class ContaBancaria:
    def __init__(self,titular):
        self.titular=titular
        self._saldo=0

    def depositar(self,valor):
        self._saldo += valor 
        return self._saldo

    def sacar (self,valor):
        if(self._saldo>=valor):
            self._saldo -=valor
            return self._saldo 
        else:
            return f"saldo insuficiente! {self._saldo}"
    def mostra_saldo(self):
        return (f"a conta da {self.titular} possui {self._saldo} R$.")
class Contacc(ContaBancaria):
    def __init__(self, titular):
        super().__init__(titular)
        self.__limite=200
        self._saldo+=self.__limite
    def sacar(self, valor):
        if(self._saldo<=valor):
            return f"saldo insuficiente! {self._saldo}"
        else:
            return self._saldo - valor          
class ContaPoupanca(ContaBancaria):
    def  __init__(self, titular):
        super().__init__(titular)

conta_leile= Contacc("leileane")



conta1=ContaBancaria("leileane")
print(conta1.mostra_saldo)
conta1.depositar(500)
print(conta1.mostra_saldo())
print(conta1.sacar(700))


# # print(f"a conta do {conta1.titular} possui {conta1.saldo} R$.")
