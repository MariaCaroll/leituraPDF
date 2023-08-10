# Realiza login ni systema

def func_login(var_strUsuario, var_strSenha, bot, var_strCaminhoSistem, not_found):

    bot.execute(var_strCaminhoSistem)
    # Tela de Login
    try:
        print("Realizando login..")
        if not bot.find("usuario", matching=0.97, waiting_time=10000):
            not_found("usuario")
        bot.rightClickRelative(82, 7)
        bot.paste(var_strUsuario)

        if not bot.find("senha", matching=0.97, waiting_time=10000):
            not_found("senha")
        bot.right_click_relative(74, 1)
        bot.paste(var_strSenha)

        if not bot.find("entrar", matching=0.97, waiting_time=10000):
            not_found("entrar")
        bot.right_click()
        print("Login realizado com sucesso....")
        # Fim da tela de login
    except:
        print("Erro ao fazer login..")
