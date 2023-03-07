# 3) faturamento
import json

with open('dados.json') as file:
    fatDiario = json.load(file)

    valores = []
    for dict in fatDiario:
        value = dict['valor']
        if value > 0:
            valores.append(value)

        mediaMensal = sum(valores) / len(valores)
        dias = 0
        for valor in valores:
            if valor > mediaMensal:
                dias += 1

    maxFat = max(valores)
    minFat = min(valores)

    print(f' O menor valor de faturamento ocorrido em um dia do mês foi R$ {minFat}')
    print(f' O MAIOR valor de faturamento ocorrido em um dia do mês foi R$ {maxFat}')
    print(f' Em {dias} dias do mês ocorreu valor de faturamento diário maior do que a média mensal')

