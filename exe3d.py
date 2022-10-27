import psutil

lst_todos_processos = []
soma_rss = 0


#passo 1: pegar todos os processos e calcular a média rss por processo
for p in psutil.process_iter():
    p = p.as_dict()
    pid = p['pid']
    nome = p['name']
    mem_rss = p['memory_info'].rss
    mem_vms = p['memory_info'].vms
    
    soma_rss += mem_rss
    
    
    d = {'pid': pid, 'nome': nome, 'mem_rss': mem_rss, 'mem_vms': mem_vms}
    lst_todos_processos.append(d)
    
    
media_rss = soma_rss / len(lst_todos_processos)
print(media_rss)

#passo 2: imprimir quem está 705 acima da média
perc = 70
for p in lst_todos_processos:
    if p['mem_rss'] > media_rss + media_rss * perc / 100:
        print(p)