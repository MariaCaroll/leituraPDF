   if os.path.isfile(var_strCaminhoArquivo):
        print("Removendo arquivo para inlcuir uma versão atual...")
        os.remove(var_strCaminhoArquivo)
    else:
        print('Path is not a file')