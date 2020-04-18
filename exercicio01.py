print(f"Cálculo - Area e Perímetro do retângulo")

h = float(input(f"Digite a Altura (cm): "))
b = float(input('Digite a Base (cm): '))
print('{}\n{}Resultado'.format('=' * 30, ' ' * 10))
area = b * h
perimetro = 2 * (h + b)

print(f"Area: {area}cm\nPerímetro: {perimetro}cm")
