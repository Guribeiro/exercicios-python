status = False


def printError(str):
    print(f"{25 * '--'}")
    print(f'ERROR INPUT TYPE! {str}')
    print(f"{25 * '--'}")


while(status == False):
    print(f'{10 * "-"} Calculo de Quilometragem {10 * "-"}')
    kmInitial = float(input("Informe a Quilometragem inicial: "))
    kmFinal = float(input("Informe a Quilometragem final: "))

    if(kmInitial < 0):
        printError('Tente novamente')
    else:
        if (kmInitial >= kmFinal):
            print(f"{25 * '--'}")
            print(
                'Quilometragem inicial maior do que a Quilometragem final.\nPor favor, tente novamente')
            print(f"{25 * '--'}")

        if (kmFinal > kmInitial):
            tempoGasto = int(input("Informe o tempo gasto no trajeto: "))

            if(tempoGasto <= 0):
                printError('Não foi possível calcular')
            else:
                status = True

distanciaPerc = kmFinal - kmInitial

velocVeiculo = distanciaPerc / tempoGasto

print(f"{25 * '--'}")
print(
    f'Distância percorrida: {distanciaPerc:.0f}kms\nVelocidade do veículo: {velocVeiculo:.0f}km/h')
