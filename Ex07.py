keys = []

x = int(input('Informe o primeiro número - [x]: '))
y = int(input('Informe o segundo número  - [y]: '))
z = int(input('Informe o terceiro número - [z]: '))


def listAsString(list):
    listToString = ' - '.join(map(str, list))
    return listToString

def handleIguais(a, b, c):
    if(a == b and b != c):
        data = dict()
        data['x'] = a
        data['y'] = b
        return data
    elif(b == c and c != a):
        data = dict()
        data['y'] = b
        data['z'] = c
        return data
    else:
        data = dict()
        data['x'] = a
        data['z'] = c
        return data

maior = x
menor = x

if(x != y != z != x):

    if(y < x and y < z):
        menor = y
    if(z < x and z < y):
        menor = z

    if(y > x and y > z):
        maior = y
    if(z > x and z > y):
        maior = z

    print(f"{20 * '--'}")
    print(f'Maior número: {maior}')
    print(f'Menor número: {menor}')

elif (x == y == z):
    print(f"{15 * '--'}")
    print('Os três números são iguais')
else:
    print(f"{20 * '--'}")
    iguais = handleIguais(x,y,z)
    keysIguais = iguais.keys()
    print('Apenas dois números iguais')
    for i in iguais:
        keys.append(i)
    listToString = listAsString(keys)
    print(f'Digitados iguais: {listToString}')
