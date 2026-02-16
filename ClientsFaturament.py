import pandas as pd

class Gera:
    def __init__(self, faturamento, gera):
        self.faturamento = self.LerArquivo(faturamento)
        self.gera = self.LerArquivo(gera)
    def LerArquivo(self,arquivo):
        return pd.read_excel(arquivo)
    def FiltrarFaturamento(self, filtro):
        return self.faturamento[self.faturamento['faturamento total'] > filtro]
    def ObterGera(self):
        return self.gera
    def ObterM1(self):
        return self.gera[['executivo','nível', 'm1', 'm1 meta']]
    def EnumerarExecutivos(self):
        return '\n'.join([f'({i}) {executivo}' for i, executivo in enumerate(self.gera['executivo'], start=1)])
    def ObterExecutivo(self):
        return list(self.gera['executivo'])
    def ObterGeraExecutivo(self, ExecutivoEscolhido):
        Ind = int(ExecutivoEscolhido) - 1
        Executivo = self.ObterExecutivo()[Ind]
        Filtrado = self.ObterGera()
        return Filtrado[Filtrado['executivo'] == Executivo]

