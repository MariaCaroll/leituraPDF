# Responsavel por enviar e-mail de finalização

# For e-mail
from botcity.plugins.email import BotEmailPlugin
from configuracao import var_strDestinatario


def funEnviarEmail(email, erro, horaInicio, horaFim,anexo):
    print("Criando corpo do e-mail.")
    # Definindo os atributos que compoem a mensagem
    para = [var_strDestinatario]
    assunto = "Robô finalizado"
    file = [anexo]


    corpo_email = f"<!DOCTYPE html> <html lang='pt-br'><body> <p>Olá, tudo bem?</p><p>O robô com inicio às {horaInicio} finalizou ás {horaFim} com {erro}.</p></body></html>"
    # Enviando a mensagem de e' -mail
    try:
        email.send_message(assunto, corpo_email, para,
                           attachments=file, use_html=True)
        print("E-mail enviado com sucesso!")
    except:
        print(f"Erro ao enviar e-mail para {var_strDestinatario}")

    # Feche a conexão com os servidores IMAP e SMTP
    email.disconnect()


def funConectatEmail(usuario, senha, erro, horaInicio, horaFim, anexo):
    # Instantiate the plugin
    var_strEmail = BotEmailPlugin()
    # Configure SMTP with the gmail server
    var_strEmail.configure_smtp("smtp.gmail.com", 587)
    # Login with a valid email account
    var_strEmail.login(usuario, senha)
    print("Enviando e-mail de finalização...")
    funEnviarEmail(var_strEmail, erro, horaInicio, horaFim,anexo)
