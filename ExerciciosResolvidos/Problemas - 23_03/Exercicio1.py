""" Não entendi o enunciado de primeira
Se a hora inicial for igual à hora final, significa que o jogo durou 24 horas.
Se a hora final for maior que a inicial, o jogo começou e terminou no mesmo dia.
Se a hora final for menor que a inicial, significa que o jogo passou da meia-noite.

"""

a, b = map(int, input().split())

if a == b:
    tempo = 24
elif a < b:
    tempo = b - a
else:
    tempo = (24 - a) + b

print(f"O JOGO DUROU {tempo} HORA(S)")