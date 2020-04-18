

valorSalario = float(input(f"Digite seu salário R$: "))
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
    print(f"Valor do bem inferior ou igual a {porcentMin}% do seu salário.\nSeu crédito foi Aprovado")
    
else:
    print(f"Valor do bem superior a {porcentMin}% do seu salário.\nSeu crédito foi Negado")