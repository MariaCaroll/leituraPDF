# Faz a leitura do arquivo de pdf e extrai os dados relevantes
import PyPDF2

try:
    print("Realizando a leitura do arquivo pdf..")
    # Pega o aquivo pdf
    var_arqPdf = open("fatura.pdf", "rb")
    var_readerPdf = PyPDF2.PdfReader(var_arqPdf)
    # Verifica o número de páginas
    var_intPageNumber = var_readerPdf.numPages
    var_strPage = var_readerPdf.getPage(var_intPageNumber - 1)
    # Extrai o texto
    var_strTexto = var_strPage.extractText()

    var_strCaminhoArquivo = "arquivo.txt"

    # Escreve no arquivo txt
    var_strAquivo = open(var_strCaminhoArquivo, "a")
    var_strAquivo.writelines(var_strTexto)
    print("Leitura realizado com sucesso...")

    print("Criando arquivo de texto do pdf..")
    with open(var_strCaminhoArquivo, "r") as arquivo:
        var_texto = arquivo.read()
        print("arquivo de texto criado com sucesso...")

except:
    print("Erro na leitura do arquivo PDF.")
