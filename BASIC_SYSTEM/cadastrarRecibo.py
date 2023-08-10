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


def fun_cadastrarRecibo(bot, not_found):
    try:
        print("Agora vai cadastrar..")
        if not bot.find("idCliente", matching=0.97, waiting_time=10000):
            not_found("idCliente")
        bot.right_click_relative(88, 11)

        if not bot.find("nomeCliente", matching=0.97, waiting_time=10000):
            not_found("nomeCliente")
        bot.right_click_relative(124, 6)

        if not bot.find("contato", matching=0.97, waiting_time=10000):
            not_found("contato")
        bot.right_click_relative(73, 7)

        if not bot.find("numDocumento", matching=0.97, waiting_time=10000):
            not_found("numDocumento")
        bot.right_click_relative(101, 19)

        if not bot.find("dataDocumento", matching=0.97, waiting_time=10000):
            not_found("dataDocumento")
        bot.right_click_relative(136, 3)

        if not bot.find("dataLeitura", matching=0.97, waiting_time=10000):
            not_found("dataLeitura")
        bot.right_click_relative(73, 9)

        if not bot.find("descricao", matching=0.97, waiting_time=10000):
            not_found("descricao")
        bot.right_click_relative(104, 9)

        if not bot.find("valorLiquido", matching=0.97, waiting_time=10000):
            not_found("valorLiquido")
        bot.right_click_relative(68, 5)

        if not bot.find("imposto", matching=0.97, waiting_time=10000):
            not_found("imposto")
        bot.right_click_relative(89, 9)

        if not bot.find("profissional", matching=0.97, waiting_time=10000):
            not_found("profissional")
        bot.right_click_relative(95, 8)

        if not bot.find("subTotal", matching=0.97, waiting_time=10000):
            not_found("subTotal")
        bot.right_click_relative(93, 5)

        if not bot.find("adicionar", matching=0.97, waiting_time=10000):
            not_found("adicionar")
        bot.click()

    except:
        print("Erro ao cadastrar recibo")
