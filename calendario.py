import calendar

def mostrar_calendario():
    try:
        ano = int(input("Digite o ano: "))
        mes = int(input("Digite o mês: "))
        print("\n...Calendário...")
        print(calendar.month(ano, mes))
    except ValueError:
        print("Inválido, por favor insira valores válidos")

def main():
    while True:
        print("\n...Calendário...")
        print()
        print("1. Mostrar Calendário")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            mostrar_calendario()
        elif escolha == '2':
            print("Saindo...")
            break
        else:
            print("Tecla Inválida.")
main()