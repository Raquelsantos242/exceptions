import os

def busca_arq(nome_dir, nome_arq):
    lista_dir = [nome_dir] #guarda diretórios que ainda devem ser examinados 
    lista_resp = [] #retorno da função -> diretório onde o arquivo foi encontrado
    
    
    while lista_dir: #enquanto houver conteúdo em lista_dir
        dir_atual = lista_dir[0]
        print(dir_atual)
        
        #retornar o conteúdo do diretório atual
        try:
            l = os.listdir()
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


#teste: busca arq_texto.txt em E:TESTE
pastas = busca_arq('E:/TESTE', 'arq_texto.txt')
print(pastas)