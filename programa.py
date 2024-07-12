notas = [100, 50, 10, 5, 1]

def gerarSaque(saque):
    quantidade = [0,0,0,0,0]
    for i in range(5):
        quantidade[i] = saque//notas[i]
        saque = saque - quantidade[i] * notas[i]
    return quantidade

def receberValor():
    valor = input("Insira um valor para sacar: R$ ")
    try:
        valor = int(valor)
    except :
        print("Valor inserido incorretamente")
        valor = receberValor()   
    finally:
        return valor 

while True:
    saque = receberValor()
    
    if saque >= 10 and saque <= 600:

        resposta = gerarSaque(saque)
        print("Serão impressas:")
        for i in range(5):
            print(resposta[i], " notas de R$", notas[i])
        
        resposta = input("Sacar novamente? s/n\n")
        if resposta == "n" or resposta == "N":
            print("FIM")
            break

    elif saque < 10: 
        print("Saque muito pequeno")
    else:
        print("Saque muito grande")