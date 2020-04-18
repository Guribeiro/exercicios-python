import time

notas = []
competencias = ['Regimental', 'Parcial', 'Trabalho']
title = 'Insira a nota de acordo com a competência'.upper()


def statusAluno(media):
    if media >= 6:
        return 'APROVADO'
    else:
        return 'REPROVADO'


print(f'{title}\n{"=" * 45}')

for i in range(len(competencias)):  

    if competencias[i] == 'Regimental':
        nota = float(input(f'{competencias[i]} - peso(0 à 5): '))
        if nota < 0 or nota > 5:
            print(
                f'Error!\nDigite uma nota válida. "UserInput = {nota}"\nEsse programa será encerrado em...')
            for i in range(3, 0, -1):
                time.sleep(0.8)
                print(i)
            print('Encerrado!')
            break
        else:
            notas.append(nota)
    elif competencias[i] == 'Parcial':
        nota = float(input(f'{competencias[i]} - peso(0 à 3): '))
        if nota < 0 or nota > 3:
            print(
                f'Error!\nDigite uma nota válida. "UserInput = {nota}"\nEsse programa será encerrado em...')
            for i in range(3, 0, -1):
                time.sleep(0.8)
                print(i)
            print('Encerrado!')
            break
        else:
            notas.append(nota)
    elif competencias[i] == 'Trabalho':
        nota = float(input(f'{competencias[i]} - peso(0 à 2): '))
        if nota < 0 or nota > 2:
            print(
                f'Error!\nDigite uma nota válida. "UserInput = {nota}"\nEsse programa será encerrado em...')
            for i in range(3, 0, -1):
                time.sleep(0.8)
                print(i)
            print('Encerrado!')
            break
        else:
            notas.append(nota)

if len(notas) > 2:  
    mediaAluno = sum(notas)

    statusAluno = statusAluno(mediaAluno)

    print('{0}{1}{0}'.format('=' * 7, ' STATUS '))

    print(f'ALUNO {statusAluno}\nMÉDIA FINAL: {mediaAluno}')


    if statusAluno == 'APROVADO':
        print('Parabéns')
    else:
        print('Estude mais')