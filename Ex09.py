import time

for N in range(0, 11):
    print(f"{15 * '-'} TABUADA DO {N} {15 * '-'}")
    time.sleep(0.09)
    for X in range(0,11):
        print(f'{N:2} vezes {X:2} igual a {N * X:2}')
        time.sleep(0.02) 

print('Fim da execução')
        