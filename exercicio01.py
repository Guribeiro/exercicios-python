
cores = {
    'limpa': '\033[m',
    'boldblue':'\033[1;30m',
    'boldred':'\033[1;31m',
    'boldgreen':'\033[1;32m',
    'boldyellow':'\033[1;33m',
    'boldpink':'\033[1;34m',
    'boldpurple':'\033[1;35m',
    'boldoceanblue':'\033[1;36m',
    'boldwhite':'\033[1;37m',
}

print(f"{cores['boldred']}Cálculo - Area e Perímetro do retângulo{cores['limpa']}")

h = float(input(f"{cores['boldwhite']}Digite a Altura (cm): "))
b = float(input('Digite a Base (cm): '))
print('{}\n{}Resultado'.format('=' * 30, ' ' * 10))
area = b * h
perimetro = 2 * (h + b)

print(f"Area: {area}cm\nPerímetro: {perimetro}cm{cores['limpa']}")
