# funções para manipular dados no banco
from BANCO.conexaoMySQL import var_strCursor, var_strConexao


def funSelecionarDados(var_strIdCliente, var_strDataDocumento, var_strDataPagamento, var_strSubtotal):
    try:
        result = 0
        var_strComando = f'SELECT  id_cliente, data_documento_leiturapdf, data_pagamentopdf FROM tb_leiturapdf WHERE id_cliente LIKE "{var_strIdCliente}" AND data_documento_leiturapdf LIKE "{var_strDataDocumento}" AND data_pagamentopdf LIKE "{var_strDataPagamento}"'
        print(var_strComando)
        var_strCursor.execute(var_strComando)
        retorno = var_strCursor.fetchall()
        result = len(retorno)
        return result
    except:
        print('Erro ao selecionar dados')


def funAddBanco(var_strIdCliente, var_strDesenvolvedor, var_strDescricao, var_strDataDocumento, var_strSubtotal, var_strFormaPagamento, var_strDataPagamento):
    try:
        var_strComando = f'INSERT INTO tb_leiturapdf (id_cliente, desenvolvedor_leiturapdf, descricao_servicos_leiturapdf,data_documento_leiturapdf,subtotal_leiturapdf,forma_pagamento_leiturapdf,data_pagamentopdf) VALUES ("{var_strIdCliente}", "{var_strDesenvolvedor}","{var_strDescricao}","{var_strDataDocumento}",{var_strSubtotal},"{var_strFormaPagamento}","{var_strDataPagamento}")'
        var_strCursor.execute(var_strComando)
        var_strConexao.commit()
        print(
            f'Adicionando fatura do cliente {var_strIdCliente} com valor R$ {var_strSubtotal} no banco')
    except:
        print(
            f'Erro ao adicionar dados no banco. Cliente: {var_strIdCliente} com valor R$ {var_strSubtotal}')
