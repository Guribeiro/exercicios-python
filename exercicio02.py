import string
import math


print(f"Cálculo - 2 raízes de uma equação de segundo grau")

valores = []

lista = list(string.ascii_uppercase)

for i in range(0, 3):
    num = int(input(f'Informe o valor de {lista[i]}: '))
    valores.append(num)

delta = pow((valores[1] * -1), 2) - 4 * valores[0] * valores[2]

print('{}'.format('=' * 30))
print(f'Valor de Delta: {delta}')

if delta < 0:
    print(
        f'Delta: {delta}\nDelta menor do que ZERO, a equação não possui raízes reais')
elif delta == 0:
    raiz = (valores[1] * -1) / (2 * valores[0])
    print(f'A equação tem apenas 1 raíz\nRaiz: {raiz}')
elif delta > 0:
    raiz1 = ((valores[1] * -1) + math.sqrt(delta)) / (2 * valores[0])
    raiz2 = ((valores[1] * -1) - math.sqrt(delta)) / (2 * valores[0])
    
    print(f'A equação tem 2 raízes\nRaiz 1: {raiz1:.1f}\nRaiz 2: {raiz2:.1f}')
