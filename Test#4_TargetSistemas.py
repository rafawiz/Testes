# 4) Porcentagem do faturamento total

import pandas as pd

fatMensal = [["SP", 67836.43], ["RJ", 36678.66], ["MG",29229.88], ["ES",27165.48], ["Outros",19849.53]]
df = pd.DataFrame(fatMensal, columns=['Estado', 'Valor faturamento'])

fatTotal = df['Valor faturamento'].sum()

lt = []

for i, row in df.iterrows():
    porcentagem = (row['Valor faturamento'] * 100) / fatTotal
    lt.append(porcentagem)

df['% do total'] = lt

print(df[['Estado', '% do total']])