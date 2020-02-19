## Correr con el sigueinte comando
# python tipo_variable.py
import numbers

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Te equivocaste aweonao ingresa un integer")
       continue
    else:
       return userInput
       break

def inputFloat(message):
  while True:
    try:
       userInput = float(input(message))
    except ValueError:
       print("Te equivocaste aweonao ingresa un float")
       continue
    else:
       return userInput
       break

print("""
    Tienes 10 intentos para lograr ingressar
    el tipo de informacion que se rqeuiere
    ....
""")

texto = input("Ingresa un string: ")
if type(texto) is str:
    print("Bien hueon, es un string!!")

print("+")
print("+")

num = inputNumber("Ingresa un numero tipo int: ")
print("Bien weon ingresaste un int")


print("+")

fl = inputFloat("Ahora ingres un numero tipo float: ")
print("Brillante, sobrepasaste mis espectativas")

print("+")
print("+")
print("+")

print("Finalmente lo lograste ")
