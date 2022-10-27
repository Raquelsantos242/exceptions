import os
def arq_existe(nome_dir, nome_arq):
    #gerar string com caminho completo do arquivo
    caminho_arq_completo = os.path.join(nome_dir, nome_arq)
    
    #obtém todo o conteúdo do diretório
    try:
        conteudo_dir = os.listdir(nome_dir)
    except:
        return False #diretório não existe
    
    #verifica se arquico está no diretório
    if nome_arq not in conteudo_dir:
        return False
    else:
        if os.path.isfile(caminho_arq_completo):
            return True
        else:
            return False

#teste 1 -> direrório e arquivo existem, retorna True
print(arq_existe('c:/windows/system32', 'calc.exe'))
#teste 2 -> direrório existe, mas arquivo não, retorna False
print(arq_existe('c:/windows/system32', 'calculadora.exe'))
#teste 3 -> diretório não existe, retorna false
print(arq_existe('c:/windows/system33', 'calc.exe'))