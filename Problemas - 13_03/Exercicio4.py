#em dias
idade = int(input())
ano = idade // 365
idade = idade % 365
mes = idade // 30
idade = idade % 30
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{idade} dia(s)")