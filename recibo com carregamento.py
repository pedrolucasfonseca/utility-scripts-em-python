import time

Nome = input('Nome do cliente: ')
Idade = int(input('Idade do cliente: '))
if Idade < 18:
    print("O cliente é menor de idade e não pode realizar compras.")
    exit()
Quantidade = int(input('Quantidade comprada: '))
V_Uni = float(input('Valor de cada unidade: '))
if Quantidade <= 0 or V_Uni <= 0:
    print("Quantidade ou Valor Unitário inválido.")
    exit() 
valor_total = Quantidade * V_Uni

def carregamento():
    total = 30
    for i in range(1, 101):
        blocos = int(i * total / 100)
        barra = '█' * blocos + '-' * (total - blocos)
        print(f"\r[{barra}] {i}%", end="", flush=True)
        time.sleep(0.01)

carregamento()
print("\nRecibo gerado!")
print('-----------------------------------------')
print('----------- RECIBO DE VENDA -------------')
print('-----------------------------------------')
print(f'Nome do cliente: {Nome}.')
print(f'Idade do cliente: {Idade} anos.')
print('-----------------------------------------')
print(f'Valor da Compra: {valor_total:.2f} Reais')
print('-----------------------------------------')
print('----------- RECIBO DE VENDA -------------')
print('------------ Volte Sempre! --------------')
print('-----------------------------------------')
input('Pressione Enter para sair desta tela...')
