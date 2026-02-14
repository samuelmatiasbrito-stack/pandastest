import pandas as pd
from ClientsFaturament import Gera
ConsultaGera = Gera()

while True:
    Consulta = input('--Bem Vindo ao Gera-- \n'
                     'Qual consulta você quer realizar? \n' \
'(1) Faturamento dos clientes | (2) Base Gera | (3) Metas M1 | (4) Sair: ')
    if Consulta == '1':
        ConsultaFaturamento = input('(1) Base Faturamento Geral \n' \
        '(2) Base Faturamento acima de R$10.0000: ')
        if ConsultaFaturamento == '1':
            print(ConsultaGera.faturamentototal())
            pass
        elif ConsultaFaturamento == '2':
            print(ConsultaGera.faturamento10k())
            Import = input('Importar para uma planilha Excel externa? (1) Sim | (2) Não: ')
            if Import == '1':
                NomeArquivo = input('Nome arquivo: ')
                NomePlanilha = input('Nome Planilha: ')
                print('salvando...')
                ConsultaGera.faturamento10k().to_excel(f'{NomeArquivo}.xlsx', sheet_name=NomePlanilha, index=False)
            pass
    elif Consulta == '2':
        print(ConsultaGera.geratotal())
        pass
    elif Consulta == '3':
        print(ConsultaGera.metam1())
        pass
    elif Consulta == '4':
        print('Saindo do Gera...')
        break





















