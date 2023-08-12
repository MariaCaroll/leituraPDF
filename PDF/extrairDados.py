# Extrai os dados do texto do aquivo pdf...
import re
import tabula
import pandas as pd

from BASIC_SYSTEM.cadastrarRecibo import fun_cadastrarRecibo
from BASIC_SYSTEM.listaComboBox import var_listCargo, var_listForma

lista = []
var_listDadosPDF = []
dtPDF = []
try:

    # Extraindo com tabula
    with open("arquivo.txt", "r") as arquivo:
        var_strTexto = arquivo.read()

    var_strTabelas = tabula.read_pdf("fatura.pdf", pages="all")
    df = var_strTabelas[1].values.tolist()
    var_strDescricao = ""
    var_intContador = 0

    for item in df:
        if var_intContador == 0:
            var_strAuxiliar = item[1]
        var_intContador += 1
        var_strDescricao = var_strAuxiliar + ", " + item[1]
    print(f"Descrição do(s) Serviço(s): {var_strDescricao}")

    var_strTabelas = tabula.read_pdf(
        "fatura.pdf", pages="all", pandas_options={"header": None})
    df = var_strTabelas[2].values.tolist()
    var_strImposto = df[0][1]
    print(f"Valor do imposto: R${var_strImposto}")
    var_strSubtotal = df[1][1]
    print(f"Subtotal: R${var_strSubtotal}")

    # Extraindo com REGEX
    var_strRegex = re.compile(r'(EMISSÃO:\s+)([\d]{2}\/[\d]{2}\/[\d]{4})')
    var_strDataDocumento = var_strRegex.search(var_strTexto).group(2)
    print(f"Data do documento: {var_strDataDocumento}")

    var_strRegex = re.compile(r'(TURA:\s+)([\d]+)')
    var_strNumeroFatura = var_strRegex.search(var_strTexto).group(2)
    print(f"Número da fatura: {var_strNumeroFatura}")

    var_strRegex = re.compile(r'(ENTE:\s+)([a-zA-z0-9]+)')
    var_strIdCliente = var_strRegex.search(var_strTexto).group(2)
    print(f"Id do cliente: {var_strIdCliente}")

    var_strRegex = re.compile(r'(CLIENTE:\s+)(\w+\s\w+)')
    var_strNomeCliente = var_strRegex.search(var_strTexto).group(2)
    print(f"Nome do cliente: {var_strNomeCliente}")

    var_strRegex = re.compile(r'(\([\d]{2}\)\s[\d]{5}\s\W[\d]{4})')
    var_strTelefone = var_strRegex.search(var_strTexto).group(
        1).replace(" ", "").replace(")", ") ")
    print(f"Telefone: {var_strTelefone}")

    var_strRegex = re.compile(
        r'(VENCIMENTO\s+)(\w+\s\w+)(\s+)(\w+)(\s+)(\w+\s\w+\s\w+)(\s+)([\d]{2}\/[\d]{2}\/[\d]{4})')
    var_strCargo = var_strRegex.search(var_strTexto).group(4)
    var_strRegex = re.compile(
        r'(VENCIMENTO\s+)(\w+\s\w+)(\s+)(\w+)(\s+)(\w+\s\w+\s\w+)(\s+)([\d]{2}\/[\d]{2}\/[\d]{4})')
    var_strProfissional = var_strRegex.search(var_strTexto).group(2)
    print(var_strCargo + ": " + var_strProfissional)

    var_strRegex = re.compile(
        r'(EMISSÃO:\s+)([\d]{2}\/[\d]{2}\/[\d]{4})')
    var_strDataDocumento = var_strRegex.search(var_strTexto).group(4)
    print(f"Data do documento: {var_strDataDocumento}")

    var_strRegex = re.compile(
        r'(VENCIMENTO\s+)(\w+\s\w+)(\s+)(\w+)(\s+)(\w+\s\w+\s\w+)(\s+)([\d]{2}\/[\d]{2}\/[\d]{4})')
    var_strTipoPagamento = var_strRegex.search(var_strTexto).group(6)
    print(var_strTipoPagamento)

    var_strRegex = re.compile(
        r'(VENCIMENTO\s+)(\w+\s\w+)(\s+)(\w+)(\s+)(\w+\s\w+\s\w+)(\s+)([\d]{2}\/[\d]{2}\/[\d]{4})')
    var_strDataPagamento = var_strRegex.search(var_strTexto).group(8)
    print(f"Data do pagamento: {var_strDataPagamento}")

except:
    print("Erro ao extrair dados da fatura.")
