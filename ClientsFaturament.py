import pandas as pd
PoloGeraJaneiro = pd.read_excel('polosaomiguel.xlsx')
ClientesJaneiro = pd.read_excel('faturamentoclientes.xlsx')

class Gera:
    def faturamentototal(self):
        return ClientesJaneiro[['executivo', 'id cliente', 'faturamento total']]
    def faturamento10k(self):
        Faturamento = ClientesJaneiro[ClientesJaneiro['faturamento total'] > 10000]
        return Faturamento
    def geratotal(self):
        return PoloGeraJaneiro
    def metam1(self):
        return PoloGeraJaneiro[['executivo','nível', 'm1', 'm1 meta']]
