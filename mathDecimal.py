def decimalToBinary(decimal):
  if decimal == 0:
      return '0'
  elif decimal == 1:
      return '1'
  else:
      binary_part = decimalToBinary(decimal // 2)
      remainder = decimal % 2
    
      return binary_part + str(remainder)


