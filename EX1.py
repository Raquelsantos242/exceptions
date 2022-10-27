"""
# EXERCÍCIO 1
# -----------

Escrever uma função em Python que verifica se um arquivo está ou não
no diretório. A função deve receber o diretório e o nome do arquivo a ser buscado
e deve retornar True ou False.

Escrever também um programa que obtenha do usuário
o nome do arquivo a ser procurado e o diretório de busca e chame a função para
realizar a busca e indicar se encontrou ou não o arquivo em questão.
"""
import os

def arq_existe(nome_dir, nome_arq):
    
    # gera string com o caminho completo do arquivo (diretório + nome do arquivo)
    caminho_arq_completo = os.path.join(nome_dir, nome_arq)
    
    # obtém todos os arquivos do diretório
    try:
        conteudo_dir = os.listdir(nome_dir)
    except:
        #print('Diretório não existe')
        return False
    
    # verifica se arquivo está no diretório
    if nome_arq not in conteudo_dir:
        return False
    else:
        if os.path.isfile(caminho_arq_completo):
            return True
        else:
            return False
        

# TESTE 1: diretório + arquivo que existem -> tem que imprimir True
print(arq_existe("c:/windows/system32", "calc.exe"))

# TESTE 2 (diretório existe, mas arquivo não existe -> tem que imprimir False
print(arq_existe("c:/windows/system32", "calculadora.exe"))

# TESTE 3 (diretório não existe -> vai estourar um erro
print(arq_existe("c:/windows/system33", "calc.exe"))



