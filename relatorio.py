import sys
import csv
import locale
from datetime import datetime

def formatar_valor(valor):
    return locale.currency(float(valor) / 100, grouping=True)

def formatar_data(data):
    data_obj = datetime.strptime(data, '%d%m%Y')
    return data_obj.strftime('%d/%m/%Y')

if len(sys.argv) != 3:
    print("Uso: python nome_app.py <arquivo_entrada> <arquivo_saida>")
    sys.exit(1)

# Defina a localidade para o formato de moeda desejado
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

arquivo_entrada = sys.argv[1]
arquivo_saida = sys.argv[2]

try:
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_modelo, open(arquivo_saida, 'w', newline='', encoding='utf-8') as relatorio_csv:
        fornecedor = dict()

        csv_writer = csv.writer(relatorio_csv, delimiter=';')

        header_empresa = ["Nome da Empresa", "Numero de Inscricao da Empresa", "Nome do Banco", "Nome da Rua", "Numero do Local", "Nome da Cidade", "CEP", "Sigla do Estado"]
        header_favorecido = ["Nome do Favorecido", "Data de Pagamento", "Valor do Pagamento", "Numero do Documento Atribuido pela Empresa", "Forma de Lancamento"]

        csv_writer.writerow(header_empresa)

        for linha in arquivo_modelo:
            if linha[7] == '0':  # Header de arquivo
                nome_empresa = linha[72:102].strip()
                numero_inscricao_empresa = linha[18:32]
                nome_banco = linha[102:132].strip()

                numero_inscricao_empresa_formatado = f'{numero_inscricao_empresa[:2]}.{numero_inscricao_empresa[2:5]}.{numero_inscricao_empresa[5:8]}/{numero_inscricao_empresa[8:12]}-{numero_inscricao_empresa[12:]}'

            elif linha[7] == '1':  # Header de lote
                nome_rua = linha[142:172].strip()
                numero_local = linha[172:177]
                nome_cidade = linha[192:212]
                cep = linha[212:217]
                cep_complemento = linha[217:220]
                sigla_estado = linha[220:222]
                forma_lancamento = linha[11:13]

                formas_lancamento = {
                    '01': 'Crédito em Conta Corrente',
                    '02': 'Cheque Pagamento / Administrativo',
                    '03': 'DOC/TED (1) (2)',
                    '04': 'Cartão Salário' if linha[9:11] == '30' else '',
                    '05': 'Crédito em Conta Poupança',
                    '06': 'Liberação de Títulos HSBC',
                    '07': 'Emissão de Cheque Salário',
                    '08': 'Liquidação de Parcelas de Cobrança Não Registrada',
                    '09': 'Arrecadação de Tributos Federais',
                    '10': 'OP à Disposição',
                    '11': 'Pagamento de Contas e Tributos com Código de Barras',
                    '12': 'Doc Mesma Titularidade',
                    '13': 'Pagamentos de Guias',
                    '14': 'Crédito em Conta Corrente Mesma Titularidade',
                    '16': 'Tributo - DARF Normal',
                    '17': 'Tributo - GPS (Guia da Previdência Social)',
                    '18': 'Tributo - DARF Simples',
                    '19': 'Tributo - IPTU - Prefeituras',
                    '20': 'Pagamento com Autenticação',
                    '21': 'Tributo - DARJ'
                }

                forma_lancamento_descricao = formas_lancamento.get(forma_lancamento, '')

                numero_local_formatado = numero_local.strip()
                cep_formatado = f'{cep}-{cep_complemento}'

                csv_writer.writerow([nome_empresa, numero_inscricao_empresa_formatado, nome_banco, nome_rua, numero_local_formatado, nome_cidade, cep_formatado, sigla_estado])
                csv_writer.writerow(header_favorecido)
                
            elif linha[7] == '3':
                nome_favorecido = linha[43:73].strip()
                data_pagamento = linha[93:101]
                valor_pagamento = linha[119:134]
                numero_documento_empresa = linha[73:93].strip()

                data_pagamento_obj = datetime.strptime(data_pagamento, '%d%m%Y')
                data_pagamento_formatada = data_pagamento_obj.strftime('%d/%m/%Y')
                valor_formatado = formatar_valor(valor_pagamento)

                csv_writer.writerow([nome_favorecido, data_pagamento_formatada, valor_formatado, numero_documento_empresa, forma_lancamento_descricao])

except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")

print(f"Processamento concluído. Relatório gerado em {arquivo_saida}")
