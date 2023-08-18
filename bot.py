"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
import datetime
import pandas as pd

from configuracao import var_strCaminhoSistem, var_strUsuario, var_strSenha, var_strUserGmail, var_strSenhaGmail, var_strDestinatario

from BASIC_SYSTEM.loginSistema import func_login
from BASIC_SYSTEM.cadastrarRecibo import fun_acessarTelaCadastro, fun_cadastrarRecibo
from BASIC_SYSTEM.listaComboBox import var_listCargo, var_listForma
from PDF.extrairDados import var_strIdCliente, var_strNomeCliente, var_strTelefone, var_strNumeroFatura, var_strDataDocumento, var_strProfissional
from PDF.extrairDados import var_strDataPagamento, var_strDescricao, var_strImposto, var_strCargo, var_strTipoPagamento, var_strSubtotal
from BANCO.comandosMySQL import funAddBanco, funSelecionarDados
from EMAIL.sendEmail import funConectatEmail


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    agora = datetime.datetime.now()
    agora_string = agora.strftime("%A %d %B %y %I:%M")
    var_strHoraInicio = datetime.datetime.strptime(
        agora_string, "%A %d %B %y %I:%M")
    print(f"Data hora início: {var_strHoraInicio}")

    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    # Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    # Fim da tela de login
    func_login(var_strUsuario, var_strSenha, bot,
               var_strCaminhoSistem, not_found)

    #Tela de cadastro e tela de recibo
    fun_acessarTelaCadastro(bot, not_found)

    fun_cadastrarRecibo(bot, not_found, var_listCargo, var_listForma, var_strIdCliente, var_strNomeCliente, var_strTelefone, var_strNumeroFatura, var_strDataDocumento,
                        var_strDataPagamento, var_strDescricao, var_strImposto, var_strCargo,
                      var_strProfissional, var_strTipoPagamento, var_strSubtotal)

    # Adicionar dados no banco

    var_strMsgErro = ""
    valor = 0.00
    valor = float(var_strSubtotal.replace(",", "."))
    var_strRetornoBD = funSelecionarDados(
        var_strIdCliente, var_strDataDocumento, var_strDataPagamento, valor)
    if var_strRetornoBD == 0:
        print("Adicionando logs no banco...")
        var_strProf = var_strCargo + ": " + var_strProfissional

        funAddBanco(var_strIdCliente, var_strProf, var_strDescricao,
                    var_strDataDocumento, valor, var_strTipoPagamento, var_strDataPagamento)
        var_strMsgErro = "sucesso"
    else:
        print("Erro ao adicionar logs no banco.")
        var_strMsgErro = "erro"
    
    #Adicionar logs no arquivo excel
    var_strCaminhoArquivo= "dadosRecibo.xlsx"
    var_dtRecibo = pd.DataFrame(columns=["Cliente", "Profissional","Descrição do Serviço", "Forma de Pagamento", "Data do Pagamento", "SubTotal"])
    var_strNewRow = {"Cliente": var_strNomeCliente, "Profissional":var_strProf,"Descrição do Serviço":var_strDescricao, "Forma de Pagamento":var_strTipoPagamento, "Data do Pagamento":var_strDataPagamento, "SubTotal":var_strSubtotal}
    var_dtRecibo.loc[len(var_dtRecibo)] = var_strNewRow
    var_dtRecibo.to_excel(var_strCaminhoArquivo, index=False)
 
    # Disparar email de finalização
    agora = datetime.datetime.now()
    agora_string = agora.strftime("%A %d %B %y %I:%M")
    var_strHoraFim = datetime.datetime.strptime(
        agora_string, "%A %d %B %y %I:%M")
    print(f"Data hora fim: {var_strHoraFim}")

    funConectatEmail(var_strUserGmail, var_strSenhaGmail,
                     var_strMsgErro, var_strHoraInicio, var_strHoraFim,var_strCaminhoArquivo)

    # Find Process
    if not bot.find("sair", matching=0.97, waiting_time=10000):
        not_found("sair")
    bot.right_click()
    bot.right_click()

# Uncomment to mark this task as finished on BotMaestro
# maestro.finish_task(
#     task_id=execution.task_id,
#     status=AutomationTaskFinishStatus.SUCCESS,
#     message="Task Finished OK."
# )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
