def fun_acessarTelaCadastro(bot, not_found):
    try:
        print("Acessando tela de cadastro de recibo.")
        if not bot.find("menuCadastro", matching=0.97, waiting_time=10000):
            not_found("menuCadastro")
        bot.right_click()

        if not bot.find("itemRecibo", matching=0.97, waiting_time=10000):
            not_found("itemRecibo")
        bot.right_click()
    except:
        print("Erro ao acessar tela de cadastrar recibo")


def fun_cadastrarRecibo(bot, not_found, var_listCargo, var_strIdCliente, var_strNomeCliente, var_strTelefone, var_strNumeroFatura, var_strDataDocumento,
                        var_strDataPagamento, var_strDescricao, var_strImposto, var_strCargo,
                        var_strProfissional, var_strTipoPagamento, var_strSubtotal):
    var_intContador = 0

    print("Agora vai cadastrar..")
    if not bot.find("idCliente", matching=0.97, waiting_time=10000):
        not_found("idCliente")
    bot.right_click_relative(88, 11)
    bot.paste(var_strIdCliente)

    if not bot.find("nomeCliente", matching=0.97, waiting_time=10000):
        not_found("nomeCliente")
    bot.right_click_relative(124, 6)
    bot.paste(var_strNomeCliente)

    if not bot.find("contato", matching=0.97, waiting_time=10000):
        not_found("contato")
    bot.right_click_relative(73, 7)
    bot.paste(var_strTelefone)

    if not bot.find("numDocumento", matching=0.97, waiting_time=10000):
        not_found("numDocumento")
    bot.right_click_relative(101, 19)
    bot.paste(var_strNumeroFatura)

    if not bot.find("dataDocumento", matching=0.97, waiting_time=10000):
        not_found("dataDocumento")
    bot.right_click_relative(136, 3)
    bot.paste(var_strDataDocumento)

    if not bot.find("dataLeitura", matching=0.97, waiting_time=10000):
        not_found("dataLeitura")
    bot.right_click_relative(73, 9)
    bot.paste(var_strDataPagamento)

    if not bot.find("descricao", matching=0.97, waiting_time=10000):
        not_found("descricao")
    bot.right_click_relative(104, 9)
    bot.paste(var_strDescricao)

    if not bot.find("valorLiquido", matching=0.97, waiting_time=10000):
        not_found("valorLiquido")
    bot.right_click_relative(68, 5)
    var_strValorLiquido = int(var_strSubtotal) - int(var_strImposto)
    bot.paste(var_strValorLiquido)

    if not bot.find("imposto", matching=0.97, waiting_time=10000):
        not_found("imposto")
    bot.right_click_relative(89, 9)
    bot.paste(var_strImposto)

    if not bot.find("profissional", matching=0.97, waiting_time=10000):
        not_found("profissional")
    bot.right_click_relative(95, 8)
    bot.paste(var_strProfissional)

    if not bot.find("subTotal", matching=0.97, waiting_time=10000):
        not_found("subTotal")
    bot.right_click_relative(93, 5)
    bot.paste(var_strSubtotal)

    if not bot.find("adicionar", matching=0.97, waiting_time=10000):
        not_found("adicionar")
    # bot.right_click()

    # Selecionar cargo
    if not bot.find("cargo", matching=0.97, waiting_time=10000):
        not_found("cargo")
    bot.right_click_relative(67, 9)
    var_intIndex = var_listCargo.index(var_strCargo)
    while var_intContador <= var_intIndex:
        bot.type_down()
