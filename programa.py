class Caixa():
    def __init__(self):
        self.notas = [100, 50, 10, 5, 1]
        self.min = 10
        self.max = 600

    def receberValor(self):
        valor = input("Insira um valor para sacar: R$ ")
        try:
            valor = int(valor)
        except :
            print("Valor inserido incorretamente")
            valor = self.receberValor()   
        finally:
            return valor 

    def gerarSaque(self, saque):
        quantidade = [0,0,0,0,0]
        for i in range(5):
            quantidade[i] = saque//self.notas[i]
            saque = saque - quantidade[i] * self.notas[i]
        return quantidade
    
    def saque(self):
        valor_sacado = self.receberValor()

        if valor_sacado >= self.min and valor_sacado <= self.max:
            resposta = self.gerarSaque(valor_sacado)
            print("Serão impressas:")
            for i in range(5):
                print(resposta[i], " notas de R$", notas[i])
            
            resposta = input("Sacar novamente? s/n\n")
            if resposta == "n" or resposta == "N":
                print("FIM")
        
        elif valor_sacado < self.min:
            print(f"Saque insuficiente.\n(minimo = {self.min})")
        else:
            print(f"Saque excedente.\n(maximo = {self.max})")
                
caixa = Caixa()
caixa.saque()