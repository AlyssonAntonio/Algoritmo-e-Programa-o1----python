hi, mi, hf, mf = map(float, input().split())

ini = hi*60+mi
fim = hf*60+mf

if ini == fim:
    duracao = 24 * 60
elif fim > ini:
    duracao = fim - ini
else:
    duracao = (24*60-ini)+fim

horas=duracao//60
minutos=duracao%60

print(f"O JOGO DUROU {horas:.0f} HORA(S) E {minutos:.0f} MINUTO(S)")

