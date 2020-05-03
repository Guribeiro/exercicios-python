from datetime import date
anoAtual = date.today().year
print(f'{10 * "-"} Verificador de Ano bissexto {10 * "-"}')
print('Digite [0] para verificar o ano atual ou\ninforme abaixo o ano desejado no formato - [XXXX]')
print(f'{50 * "-"}')
anoInput = int(input('Informe um Ano para analisar: '))


def verifyLeapYear(year):
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print(f'O ano de {year} é Bissexto')
    else:
        print(f'O ano de {year} não é Bissexto')

if anoInput == 0:
    anoInput = anoAtual

if(anoInput == anoAtual):
    verifyLeapYear(anoInput)
else:
    verifyLeapYear(anoInput)

