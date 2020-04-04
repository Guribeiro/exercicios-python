import string
import math
cores = {
    'limpa': '\033[m',
    'boldblue': '\033[1;30m',
    'boldred': '\033[1;31m',
    'boldgreen': '\033[1;32m',
    'boldyellow': '\033[1;33m',
    'boldpink': '\033[1;34m',
    'boldpurple': '\033[1;35m',
    'boldoceanblue': '\033[1;36m',
    'boldwhite': '\033[1;37m',
}

print(f"{cores['boldblue']}Cálculo - 2 raízes de uma equação de segundo grau{cores['limpa']}")

valores = []

a = list(string.ascii_uppercase)

for i in range(0, 3):

    num = int(input(f'{cores["boldwhite"]}Informe o valor de {a[i]}: '))
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
    
    print(f'A equeção tem 2 raízes\nRaiz 1: {raiz1:.1f}\nRaiz 2: {raiz2:.1f}')
