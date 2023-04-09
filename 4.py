"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP _ R$67.836,43
RJ _ R$36.678,66
MG _ R$29.229,88
ES _ R$27.165,48
Outros _ R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro 
do valor total mensal da distribuidora.
"""

estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamentoTotal = sum(estados.values())
print(f"Faturamento total: R$ {faturamentoTotal:.3f} reais")

print('Faturamento por estado:')
for estado, faturamento in estados.items():
    percentual = (faturamento / faturamentoTotal) * 100
    print(f"{estado}: {percentual:.2f}%")

