import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError
    elif operador == '**':
        result = num1 ** num2
    else:
        raise ValueError("Operação inválida")
    return result

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')

            num1 = float(input('Digite o primeiro número:'))
            num2 = float(input('Digite o segundo número: '))
            operador = input('Escolha a operação (+, -, *, /, **): ')

            resultado = calculadora(num1, num2, operador)
            print(f'\nResultado: {resultado}\n')

            continuar = input('Deseja continuar? (s/n): ').strip().lower()
            if continuar != 's':
                break

        except ValueError as e:
            print(f'Erro: {e} -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
  
