import pandas as pd
PoloGeraJaneiro = pd.read_excel('polosaomiguel.xlsx')
ClientesJaneiro = pd.read_excel('faturamentoclientes.xlsx')

class Gera:
    def __init__(self, faturamento, gera):
        self.faturamento = self.LerArquivo(faturamento)
        self.gera = self.LerArquivo(gera)
    def LerArquivo(self,arquivo):
        return pd.read_excel(arquivo)
    def FiltrarFaturamento(self, filtro):
        return ClientesJaneiro[ClientesJaneiro['faturamento total'] > filtro]
    def ObterGera(self):
        return PoloGeraJaneiro
    def ObterM1(self):
        return PoloGeraJaneiro[['executivo','nível', 'm1', 'm1 meta']]
    def ObterExecutivos(self):
        return '\n'.join([f'({i}) {executivo}' for i, executivo in enumerate(PoloGeraJaneiro['executivo'], start=1)])
    
