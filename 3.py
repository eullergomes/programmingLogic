"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na 
linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser 
ignorados no cálculo da média;
"""


import json

with open("./json/dados.json") as dados:
    faturamento = json.load(dados)

menor_faturamento = float('inf')
maior_faturamento = float('-inf')

#média mensal de faturamento 
soma_faturamento = 0
dias_com_faturamento = 0
for dia in faturamento:
    if dia['valor'] > 0: #ignorando os dias sem faturamento
        soma_faturamento += dia['valor']
        dias_com_faturamento += 1
media_mensal = soma_faturamento / dias_com_faturamento

#dias em que o faturamento diário foi maior do que a média mensal
dias_acima_da_media = 0
for dia in faturamento:
    if dia['valor'] > media_mensal:
        dias_acima_da_media += 1

    # Atualizar o menor e maior faturamento diário
    if dia['valor'] < menor_faturamento:
        menor_faturamento = dia['valor']
    if dia['valor'] > maior_faturamento:
        maior_faturamento = dia['valor']

print('Menor faturamento do dia: R$ {:.2f}'.format(menor_faturamento))
print('Maior faturamento do dia dia: R$ {:.2f}'.format(maior_faturamento))
print('Dias com faturamento acima da média mensal: {}'.format(dias_acima_da_media))
