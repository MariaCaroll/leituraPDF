# funções para manipular dados no banco
from BANCO.conexaoMySQL import var_strCursor, var_strConexao


def funSelecionarDados(var_strIdCliente, var_strDataDocumento, var_strDataProcessamento, var_strSubtotal):
    result = 0
    try:
        var_strComando = f'SELECT id_cliente, data_documento_leiturapdf, date_leiturapdf, subtotal_leiturapdf FROM tb_leiturapdf WHERE wiid_workItem LIKE "{var_strIdCliente}, {var_strDataDocumento},{var_strDataProcessamento},{var_strSubtotal}"'
        var_strCursor.execute(var_strComando)
        retorno = var_strCursor.fetchall()
        result = len(retorno)
        return result
        # print(result)
    except:
        print('Erro ao selecionar dados')


def funAddBanco(var_strIdCliente,var_strDesenvolvedor,var_strDescricao,var_strDataDocumento, var_strSubtotal, var_strFormaPagamento, var_strDataProcessamento):
    try:
        var_strComando = f'INSERT INTO tb_leiturapdf (id_cliente, desenvolvedor_leiturapdf, descricao_servicos_leiturapdf,data_documento_leiturapdf,subtotal_leiturapdf,forma_pagamento_leiturapdf,date_leiturapdf) VALUES ("{var_strIdCliente}", "{var_strDesenvolvedor}","{var_strDescricao}","{var_strDataDocumento}","{var_strSubtotal},"{var_strFormaPagamento},"{var_strDataProcessamento}")'
        var_strCursor.execute(var_strComando)
        var_strConexao.commit()
        print(f'Adicionando fatura do cliente {var_strIdCliente} com valor R$ {var_strSubtotal} no banco')
    except:
        print(f'Erro ao adicionar dados no banco. Cliente: {var_strIdCliente} com valor R$ {var_strSubtotal}')
