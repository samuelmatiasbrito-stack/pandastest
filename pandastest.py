import pandas as pd
df = pd.read_excel('basesalário.xlsx')
# print(df.head())
salarios = df['salário']
mais5k = df[df['salário'] > 5000]
mais13k = df[df['salário'] > 13000]
print(mais5k[['nome', 'salário']])
print(mais13k[['nome', 'salário']])