import pandas as pd
PoloGeraJaneiro = pd.read_excel('polosaomiguel.xlsx')
ClientesJaneiro = pd.read_excel('faturamentoclientes.xlsx')

class Gera:
    def obterfaturamento(self):
        return ClientesJaneiro[['executivo', 'id cliente', 'faturamento total']]
    def filtrarfaturamento(self, filtro):
        return ClientesJaneiro[ClientesJaneiro['faturamento total'] > filtro]
    def obtergera(self):
        return PoloGeraJaneiro
    def obterm1(self):
        return PoloGeraJaneiro[['executivo','nível', 'm1', 'm1 meta']]
