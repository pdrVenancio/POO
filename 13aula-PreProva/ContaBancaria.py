from datetime import date

class Conta:
    def __init__(self, nroConta, nome, limite, senha): #AGREGAÇÃO = LISTA
        self._nroConta = nroConta
        self._nome = nome
        self._limite = limite
        self._senha = senha
        self._transacoes = [] #agrega todas as transações realizadas por meio de uma lista chamada transacoes
    
    @property
    def nroConta(self):
        return self._nroConta
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def senha(self):
        return self._senha
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionaDeposito(self, valor, data, nomeDepositante):
        t1 = Deposito(valor, data, nomeDepositante)
        self.transacoes.append(t1)
    
    def adicionaSaque(self, valor, data, senha):
        if senha != self.senha or self.calculaSaldo() < valor:
            return False
        
        s1 = Saque(valor, data, senha)
        self.transacoes.append(s1)
        return True

    # Tranferencia / Saque = Retirar dinheiro
    # Deposito = Colocar dinheiro
    # Debito = Quem perde
    # Credito = Quem ganha

    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha != self.senha or self.calculaSaldo() < valor:
            return False

        tDebito = Transferencia(valor, data, senha, "D")
        self.transacoes.append(tDebito)
        tCredito = Transferencia(valor, data, senha, "C")
        contaFavorecido.transacoes.append(tCredito)
        return True
        
    def calculaSaldo(self):
        saldo = self.limite
        for transacoes in self.transacoes:
            if type(transacoes) == Saque:
                saldo = saldo - transacoes.valor
            elif type(transacoes) == Deposito:
                saldo = saldo + transacoes.valor
            elif type(transacoes) == Transferencia:
                if transacoes.tipoTransf == "D":
                    saldo = saldo - transacoes.valor
                elif transacoes.tipoTransf == "C":
                    saldo = saldo + transacoes.valor
        
        return saldo

class Transacao:
    def __init__(self, valor, data):
        self._valor = valor
        self._data = data
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def data(self):
        return self._data
    
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self._senha = senha

    @property
    def senha(self):
        return self._senha

class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self._senha = senha
        self._tipoTransf = tipoTransf
    
    @property
    def senha(self):
        return self._senha
    
    @property
    def tipoTransf(self):
        return self._tipoTransf

class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self._nomeDepositante = nomeDepositante

    @property
    def nomeDepositante(self):
        return self._nomeDepositante

if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800') 
    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 170
