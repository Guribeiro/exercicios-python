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

valorSalario = float(input(f"{cores['boldwhite']}Digite seu salário R$: "))
valorBem = float(input('Digite o valor do bem R$: '))
porcentMin = 30

def verificaCredito (sal, valorBem):

    if valorBem > (sal / 100) * porcentMin:
        return False
    else:
        return True 

status = verificaCredito(valorSalario, valorBem)
print('{0}{1}{0}'.format('=' * 7, ' STATUS '))

if status == True:
    print(f"Valor do bem inferior a {porcentMin}% do seu salário.\nSeu crédito foi {cores['limpa']}{cores['boldblue']}Aprovado{cores['limpa']} {cores['boldwhite']}")
    
else:
    print(f"Valor do bem superior a {porcentMin}% do seu salário.\nSeu crédito foi {cores['boldred']}Negado{cores['limpa']}")