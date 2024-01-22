
#PRIMEIRA VERSAO
def calculadora():
    while True:
        try:  # executa o codigo
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            operador = input("digite o operador")

            if operador == '+':
                resultado = n1 + n2
                print("A soma dos dois números é:", resultado)
            elif operador == '-':
                resultado = n1 - n2
                print("A subtração dos dois números é:", resultado)
            elif operador == '*':
                resultado = n1 * n2
                print("O produto dos dois números é:", resultado)
            elif operador == '/':
                if n2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = n1 / n2
                    print("A divisão dos dois números é:", resultado)
            else:
                print("Operador inválido. Por favor, use '+', '-', '*' ou '/'.")

            continuar = input("Deseja fazer outra operação? (S/N): ").upper()
            if continuar != 'S':
                break

        except ValueError:
            print("Isso não é um número. Por favor, tente novamente.")

#==================================================================================================================
#VERSÃO POLIDA E ATUALIZADA:
def calculadora2():
    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            operador = input("Digite o operador: ")

            if operador in ('+', '-', '', '/'):
                resultado = eval(f"{n1} {operador} {n2}")
                if operador == '/' and n2 == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
                print(f"O resultado da operação é: {resultado}")
            else:
                raise ValueError("Operador inválido. Por favor, use '+', '-', '' ou '/'.")

            continuar = input("Deseja fazer outra operação? (S/N): ").lower()
            if continuar != 's':
                break

        except Exception as e:
            print(f"Erro: {e}. Por favor, tente novamente.")


#==================================================================================================================
while True:
    print("bem vindo ao teste da calculadora")
    versao = input("qual versão deseja usar? (v1 ou v2)")

    if versao == "" or versao == "1" or versao == "v1":
        calculadora()
        break
    elif versao == "2" or versao == "v2":
        calculadora2()
        break

        print("Saindo. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")