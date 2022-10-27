"""
# EXERCÍCIO 2
# -----------

Escreva uma função semelhante a do Exercício 1 para buscar um arquivo
recursivamente a partir de um diretório. Faça, agora, a função retornar uma
lista de diretórios que contém o arquivo. Se a lista estiver vazia, indica que
não encontrou. Escreva também um programa que obtenha do usuário o nome do
arquivo e do diretório e chame a função para buscar o arquivo no diretório em
questão. Quando terminar, indique em que diretórios o arquivo foi encontrado.
"""
import os

def busca_arq_recursivo(nome_dir, nome_arq):
    
    lista_dir = [nome_dir]  # guarda diretórios que ainda devem ser buscados
    lista_resp = [] # retorno da função -> diretórios onde arquivo foi encontrado
    
    while lista_dir: # enquanto houver conteudo em lista_dir
        dir_atual = lista_dir[0]

        # retorna conteudo do diretório atual
        try:
            l = os.listdir(dir_atual)
        except:
            l = []
        
        for nome in l:
            caminho_completo = os.path.join(dir_atual, nome)
            
            if os.path.isfile(caminho_completo):
                if nome.upper() == nome_arq.upper():
                    lista_resp.append(caminho_completo)
            else:
                lista_dir.append(caminho_completo)
            
        lista_dir.remove(dir_atual)
    
    return lista_resp
        
        

# TESTE 1: diretório + arquivo que existem -> tem que imprimir True
print(busca_arq_recursivo("d:\\teste", "readme.txt"))




