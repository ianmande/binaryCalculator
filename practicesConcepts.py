myName = "Nicolas"

print(myName, ' Hola')

#myName = input("Cual es tu nombre ")

print(myName, ' Hola')

#template string

template = 'Hola {}, como estas'.format(myName)
template = f'Hola {myName}, como estas v2'

print(template)


def message_creator(text):
  options = {
      "computadora": "Con mi computadora puedo programar usando Python",
      "celular": "En mi celular puedo aprender usando la app de Platzi",
      "cable": "¡Hay un cable en mi bota!",
  }
  if (text in options.keys):
    return options[text]
  else:
    return 'Artículo no encontrado'


text = 'computadora'
response = message_creator(text)
print(response)
