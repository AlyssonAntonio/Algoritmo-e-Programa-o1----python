"""
Cod_Peca = int(input())
Num_Unidades = int(input())
Valor_Unitario = float(input())
"""
Cod_Peca1, Num_Unidades1, Valor_Unitario1 = input().split()
Cod_Peca2, Num_Unidades2, Valor_Unitario2 = input().split()

#Só converti de texto para valor, float ou interiro, lero lero lerooo!
Num_Unidades1 = int(Num_Unidades1)
Num_Unidades2 = int(Num_Unidades2)
Valor_Unitario1 = float(Valor_Unitario1)
Valor_Unitario2= float(Valor_Unitario2)

soma = (Num_Unidades1 * Valor_Unitario1)+(Num_Unidades2 * Valor_Unitario2)


print(f"VALOR A PAGAR: R$ {soma:.2f}")