import random

def jogo_numero_secreto():
    menor_valor = 1
    maior_valor = 50
    numero_secreto = random.randint(menor_valor, maior_valor)
    tentativas = 0

    print(f"Bem vindo ao jogo do Número Secreto!")
    print(f"Estou pensando em um número de {menor_valor} a {maior_valor}...")

    while True:
        try:
            palpite = int(input("Escolha um número:" ))
            tentativas += 1

            if palpite < menor_valor or palpite > maior_valor:
                print(f"Seu palpite está fora do número de ({menor_valor} a {maior_valor}). Por favor, tente novamente.")
            elif palpite < numero_secreto:
                print("Muito baixo! Tente novamente!")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente!")
            else:
                print(f"Parabéns! Você escolheu o número {numero_secreto} em {tentativas} tentativas!")
                break
        except ValueError:
            print("Valor inválido, por favor tente um número inteiro.")

if __name__ == "__main__":
    jogo_numero_secreto()