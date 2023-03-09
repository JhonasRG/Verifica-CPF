import re
import sys

CPF = input("Insira seu CPF: ")
CPF = re.sub(
   r'[^0-9]', '', CPF
)

digitos_sequenciais = False

try:
   digitos_sequenciais = CPF == CPF[0] * len(CPF)
except IndexError:
   print("Insira números")
   sys.exit()

if digitos_sequenciais:
   print("Você inseriu dados inválidos")
   sys.exit()

if len(CPF) > 14:
   print("Você inseriu muitos números")
   sys.exit()
elif len(CPF) < 11:
   print("Você inseriu poucos números")
   sys.exit()


nove_digitos = CPF[:9]
contador = 10
resultado_multiplicação = 0

for numero in nove_digitos:
   while contador >= 2:
      numero = int(numero)
      resultado_multiplicação += (numero * contador)
      contador -= 1
      break

digito = (resultado_multiplicação * 10) % 11
digito = digito if digito <= 9 else 0

resultado_mult_segundo_digito = 0
segundo_contador = 11
dez_digitos = nove_digitos + str(digito)

for numero2 in dez_digitos:
   while segundo_contador >= 2:
      numero2 = int(numero2)
      resultado_mult_segundo_digito += (numero2 * segundo_contador)
      segundo_contador -= 1
      break

segundo_digito = (resultado_mult_segundo_digito * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

CPF_Validado = f'{nove_digitos}{digito}{segundo_digito}'

if CPF_Validado == CPF:
   print(f"O CPF {CPF_Validado} É Válido!")
else:
   print(f"O CPF {CPF} É Inválido")