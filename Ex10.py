status = True
import os

def convertCelsiusToFahren(grausCelsius):
    fahrennheit = (grausCelsius * 1.8) + 32 
    return fahrennheit

def printErrorMessage(message):
    print(f'{50 * "-"}')
    print(f'{message}')
    print(f'{50 * "-"}')

def handleContinue():
    print('Deseja Repetir?\nSIM - [s] ou [S]\nNÃO - [n] ou [N]')
    resp = str(input(': ')).upper().strip()
    
    while(resp != 'N' and resp != 'S'):
        os.system('clear')
        printErrorMessage('Comando inválido, tente novamente')
        print('Deseja Repetir?\nSIM - [s] ou [S]\nNÃO - [n] ou [N]')
        resp = str(input(': ')).upper().strip()
    
    if(resp == 'N'):
            print('Fim da execução')
            return False
    if(resp == 'S'):
            return True

def verifyType(celsiusInput):
    if(type(celsiusInput) == type(2)):
        return True

while(status):
    print(f"{15 * '-'} Conversor de Temperatura {15 * '-'}")
    celsiusInput = int(input('Digite a temperatura em Celsius: '))

    if(celsiusInput < 0):
        os.system('clear')
        printErrorMessage('Não foi possível calcular. Informe um valor válido')

    elif(celsiusInput >=1):
        for index in range(0, celsiusInput + 1):
            convertedValue = convertCelsiusToFahren(index)
            print(f'{index:2}°Celsius igual a {convertedValue:.1f}°Fahrenheit')
            status = False            
        print(f"{10 * '-'} Fim da conversão {10 * '-'}")
        status = handleContinue()
            

            