import pandas as pd
df = pd.read_excel('polosaomiguel.xlsx')

df2 = pd.read_excel('faturamentoclientes.xlsx')
print(df2)

Faturamento10k = df2[df2['faturamento total'] >= 10000]
print(Faturamento10k)
Faturamento10k.to_excel('clientesfaturamento10k.xlsx', sheet_name='faturamento_atingido', index= False)

BonusGeraMP = df[(df['ponto gera'] > 1000) & (df['nível'] == 'MP')]
print('Bônus Meta GERA MP:')
print(BonusGeraMP[['executivo','ponto gera']])
print('-' * 25)
BonusGeraVIP = df[(df['ponto gera'] > 1400) & (df['nível'] == 'VIP')]
print('Bônus Meta GERA VIP:')
print(BonusGeraVIP[['executivo','ponto gera']])
print('-' * 25)
BonusM1Vip = df[(df['m1'] >= df['m1 meta']) & (df['nível'] == 'VIP')]
print('Bônus Meta M1 VIP:')
print(BonusM1Vip[['executivo','m1', 'm1 meta']])
print('-' * 25)
BonusM1MP = df[(df['m1'] >= df['m1 meta']) & (df['nível'] == 'MP')]
print('Bônus Meta M1 VIP:')
print(BonusM1MP[['executivo','m1', 'm1 meta']])






















