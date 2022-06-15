#  Capturando dados
arquivo_modelo = open('modelo_arquivo.txt', 'r')
print('Abrindo arquivo')
fornecedor = dict()

for linha in arquivo_modelo:
    if linha[7] == '0':  # Header de arquivo
        nome_empresa = linha[72:102]
        print('Nome da empresa: ', nome_empresa)  # - Nome da Empresa
        numero_inscricao_empresa = linha[18:32]
        print('Número de inscrição da Empresa: ', numero_inscricao_empresa)  # - Número de Inscrição da Empresa formatado, exemplo: 00.000.000/0001-00
        nome_banco = linha[102:132]
        print('Nome do banco: ', nome_banco)  # - Nome do Banco
    elif linha[7] == '1':  # Header de lote
        nome_rua = linha[142:172]
        print('Nome da rua: ', nome_rua)  # - Nome da Rua
        numero_local = linha[172:177]
        print('Número do local: ', numero_local)  # - Número do Local formatado, exemplo: 00000
        nome_cidade = linha[192:212]
        print('Nome da Cidade: ', nome_cidade)  # - Nome da Cidade
        cep = linha[212:217]
        print('CEP :', cep)  # - CEP formatado, exemplo: 00000-000
        cep_complemento = linha[217:220]
        print('Complemento CEP: ', cep_complemento)
        sigla_estado = linha[220:222]
        print('Sigla do Estado: ', sigla_estado)  # - Sigla do Estado
        forma_lancamento = linha[11:13]
        if forma_lancamento == '01':
            forma_lancamento = 'Crédito em Conta Corrente'
        elif forma_lancamento == '02':
            forma_lancamento = 'Cheque Pagamento / Administrativo'
        elif forma_lancamento == '03':
            forma_lancamento = 'DOC/TED (1) (2)'
        elif forma_lancamento == '04' and linha[9:11] == '30':
            forma_lancamento = 'Cartão Salário'
        elif forma_lancamento == '05':
            forma_lancamento = 'Crédito em Conta Poupança'
        elif forma_lancamento == '06':
            forma_lancamento = 'Liberação de Títulos HSBC'
        elif forma_lancamento == '07':
            forma_lancamento = 'Emissão de Cheque Salário'
        elif forma_lancamento == '08':
            forma_lancamento = 'Liquidação de Parcelas de Cobrança Não Registrada'
        elif forma_lancamento == '09':
            forma_lancamento = 'Arrecadação de Tributos Federais'
        elif forma_lancamento == '10':
            forma_lancamento = 'OP à Disposição'
        elif forma_lancamento == '11':
            forma_lancamento = 'Pagamento de Contas e Tributos com Código de Barras'
        elif forma_lancamento == '12':
            forma_lancamento = 'Doc Mesma Titularidade'
        elif forma_lancamento == '13':
            forma_lancamento = 'Pagamentos de Guias'
        elif forma_lancamento == '14':
            forma_lancamento = 'Crédito em Conta Corrente Mesma Titularidade'
        elif forma_lancamento == '16':
            forma_lancamento = 'Tributo - DARF Normal'
        elif forma_lancamento == '17':
            forma_lancamento = 'Tributo - GPS (Guia da Previdência Social)'
        elif forma_lancamento == '18':
            forma_lancamento = 'Tributo - DARF Simples'
        elif forma_lancamento == '19':
            forma_lancamento = 'Tributo - IPTU - Prefeituras'
        elif forma_lancamento == '20':
            forma_lancamento = 'Pagamento com Autenticação'
        elif forma_lancamento == '21':
            forma_lancamento = 'Tributo - DARJ'
        print('Forma de lançamento convertida para sua descrição: ', forma_lancamento)  # - Forma de Lançamento convertida para a sua descrição
    elif linha[7] == '3':
        nome_favorecido = linha[43:73]
        print('Nome do Favorecido: ', nome_favorecido)  # - Nome do Favorecido
        data_pagamento = linha[93:101]
        print('Data de pagamento: ', data_pagamento)  # - Data de Pagamento formatada, exemplo: 07/06/2017 (dd/mm/aaaa)
        fornecedor['nome_favorecido'] = nome_favorecido
        fornecedor['data_pagamento_formatado'] = data_pagamento
        valor_pagamento = linha[119:134]
        print('Valor do pagamento: ', valor_pagamento)  # - Valor do Pagamento formatado, exemplo: R$ 1.000,00
        fornecedor['valor_pagamento'] = valor_pagamento
        numero_documento_empresa = linha[73:93]
        print('Número do Documento Atribuído pela Empresa: ', numero_documento_empresa)  # - Número do Documento Atribuído pela Empresa
        fornecedor['numero_documento_empresa'] = numero_documento_empresa
numero_inscricao_empresa_formatado = (f'{numero_inscricao_empresa[:2]}.{numero_inscricao_empresa[2:5]}.{numero_inscricao_empresa[5:8]}/{numero_inscricao_empresa[8:12]}-{numero_inscricao_empresa[12:]}')
numero_local_formatado = numero_local.strip().zfill(5)
cep_formatado = (f'{cep}-{cep_complemento}')


arquivo_modelo.seek(0)
arquivo_modelo.close()

