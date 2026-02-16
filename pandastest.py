from ClientsFaturament import Gera
ConsultaGera = Gera()

while True:
    Consulta = input('--Bem Vindo ao Gera-- \n'
                     'Qual consulta você quer realizar? \n' \
'(1) Faturamento dos clientes | (2) Base Gera | (3) Metas M1 | (4) Sair: ')
    if Consulta == '1':
        FiltroFaturamento = int(input('Mínimo de faturamento: R$'))
        print(ConsultaGera.FiltrarFaturamento(FiltroFaturamento))
        Export = input('Exportar para uma planilha Excel externa? (1) Sim | (2) Não: ')
        if Export == '1':
            NomeArquivo = input('Nome arquivo: ')
            NomePlanilha = input('Nome Planilha: ')
            print('salvando...')
            ConsultaGera.FiltrarFaturamento().to_excel(f'{NomeArquivo}.xlsx', sheet_name=NomePlanilha, index=False)
        pass
    elif Consulta == '2':
        FiltrarExecutivo = input('Deseja filtrar algum executivo? (1) Sim | (2) Não: ')
        if FiltrarExecutivo == '1':
            print(ConsultaGera.ObterExecutivos())
            

        elif FiltrarExecutivo == '2':
            print(ConsultaGera.ObterGera())
        pass
    elif Consulta == '3':
        print(ConsultaGera.ObterM1())
        pass
    elif Consulta == '4':
        print('Saindo do Gera...')
        break





















