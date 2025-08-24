import time

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: ")) 
operacao = input("Digite a operação: ")

match operacao:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        if num2 == 0:
            res = "Erro: Divisão por zero, tente novamente"
        else:
            res = num1 / num2
    case _:
        res = "Operação Inválida, tente novamente!"

def carregamento():
    total = 30
    for i in range(1, 101):
        blocos = int(i * total / 100)
        barra = '█' * blocos + '-' * (total - blocos)
        print(f"\r[{barra}] {i}%", end="", flush=True)
        time.sleep(0.01)

carregamento()
print("\nCarregamento concluído!")
print(f"resultado é igual a: {res}!")