from functools import reduce
import re


class Binary:
  numberBinary = "0"

  def __init__(self, numberBinary="0"):
    rgx = re.compile('^[01]+$')

    if rgx.fullmatch(numberBinary):
      print(self.numberBinary)
      self.numberBinary = numberBinary
    else:
      print('\n Un numero binario solo esta compuesto por ceros y unos')

  def convertBinaryToDecimal(self):
    listBinary = list(self.numberBinary)
    listBinary.reverse()

    binaryPower = [
        int(base) * pow(2, index) for index, base in enumerate(listBinary)
    ]

    decimal = reduce(lambda old, next: old + next, binaryPower)

    print(decimal)

  def addition(self, binary2):
    binary1 = self.numberBinary
    max_length = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_length)
    binary2 = binary2.zfill(max_length)

    carry = 0
    result = ''

    for i in range(max_length - 1, -1, -1):
      bit_sum = int(binary1[i]) + int(binary2[i]) + carry

      result = str(bit_sum % 2) + result

      print(f"\n {bit_sum % 2}")

      carry = bit_sum // 2

    if carry:
      result = '1' + result

    return result

  def subtraction(self, binary2):
    binary1 = self.numberBinary

    max_length = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_length)
    binary2 = binary2.zfill(max_length)

    binary2_list = list(binary2)
    binary2_list.reverse()
    inverted_binary = ''.join(binary2_list)

    result = self.addition(inverted_binary)

    return result.zfill(max_length)

  def multiplication(self, binary2):
    binary1 = self.numberBinary
    decimal_result = int(binary1, 2) * int(binary2, 2)
    binary_result = bin(decimal_result)[2:]
    return binary_result

  def division(self, binary2):
    binary1 = self.numberBinary
    decimal_result = int(binary1, 2) // int(binary2, 2)
    binary_result = bin(decimal_result)[2:]
    return binary_result