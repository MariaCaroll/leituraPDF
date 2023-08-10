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

from configuracao import var_strCaminhoSistem, var_strUsuario, var_strSenha

from BASIC_SYSTEM.loginSistema import func_login
from BASIC_SYSTEM.cadastrarRecibo import fun_acessarTelaCadastro

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
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

    # Tela de cadstro
    fun_acessarTelaCadastro(bot, not_found)
    if not bot.find("cargo", matching=0.97, waiting_time=10000):
        not_found("cargo")
    bot.rightClickRelative(76, 12)

    bot.find_app_element()


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
