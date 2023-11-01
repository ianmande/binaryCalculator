from mathBinary import Binary
from mathDecimal import decimalToBinary


def menu():
  print('Hola! Bienvenido a la calculadora binaria ')
  print('Por favor, elige una opción:\n')
  print('1. Convertir binario a decimal')
  print('2. Convertir decimal a binario')
  print('3. Sumar binario')
  print('3. Restar binario')
  print('4. Multiplicar binario')
  print('5. Dividir binario')
  print('6. Salir')


def main():
  while True:
    menu()
    option = input('Ingresa el número de la opción: \n')

    if option == '1':
      binary = input('Ingresa un número binario: ')
      newBinary = Binary(binary)
      print(f'El equivalente decimal de {binary} es: {newBinary}')
    elif option == '2':
      decimal = int(input("Ingresa un número decimal: "))
      result = decimalToBinary(decimal)

      print(f'El equivalente binario de {decimal} es: {result}')
    elif option == '3':
      firstBinary = input("Ingresa el primer binario: ")
      secondBinary = input("Ingresa el segundo binario: ")
      result = Binary(firstBinary).addition(secondBinary)

      print(f'La suma de {firstBinary} + {secondBinary} es: {result}')
    elif option == '4':
      firstBinary = input("Ingresa el primer binario: ")
      secondBinary = input("Ingresa el segundo binario: ")
      result = Binary(firstBinary).subtraction(secondBinary)

      print(f'La resta de {firstBinary} + {secondBinary} es: {result}')
    elif option == '5':
      firstBinary = input("Ingresa el primer binario: ")
      secondBinary = input("Ingresa el segundo binario: ")
      result = Binary(firstBinary).multiplication(secondBinary)

      print(f'El multiplacion de {firstBinary} + {secondBinary} es: {result}')
    elif option == '6':
      firstBinary = input("Ingresa el primer binario: ")
      secondBinary = input("Ingresa el segundo binario: ")
      result = Binary(firstBinary).division(secondBinary)

      print(f'El division de {firstBinary} + {secondBinary} es: {result}')
    else:
      print('Opción no válida. Por favor, elige de nuevo.')


if __name__ == "__main__":
  main()
