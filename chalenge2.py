#!/usr/bin/python3
# for em modelo range para delimitar valor
# .format para dar numer exato
# .format(x+1) par somar até o limite do range
soma = 0
for x in range(4):
    
    nota = int(input("Digite nota{}: " .format(x+1)))
    soma += nota

media = soma / 4

if media >= 7:
    print("Nota {}, aprovado" .format(media))
elif media > 3:
    print("Nota {}, recuperacao" .format(media))
else:
    print("Nota {}, reprovado" .format(media))



