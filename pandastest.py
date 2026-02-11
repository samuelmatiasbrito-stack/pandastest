import pandas as pd
df = pd.read_excel('polosaomiguel.xlsx')
# print(df)
BonusVip = df[(df['ponto gera'] > 1400) & (df['nível'] == 'VIP')]
BonusMp = df[(df['ponto gera'] > 1000) & (df['nível'] == 'MP')]

print(f' Os executivos MP que bateram o bonus são: {BonusMp[['executivos']]}')
print(f'VIPs que ganharam bonus: {BonusVip[['executivos']]}')