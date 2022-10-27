# -*- coding: utf-8 -*-
"""
# EXERCÍCIO 3
# -----------

Escreva uma função em Python que indique todos processos que estão usando
a memória residente (RSS) acima de um percentual acima da média aritmética
de uso memória de todos os processos correntes. A função deve receber dois
parâmetros: a lista de todos os processos e um percentual que indica o quanto
acima da média deve estar o nível de memória. A função deve retornar uma
lista de dicionários contendo o PID, nome, memória residente (RSS) e
memória virtual (VMS) do processo.

Escreva também um programa que chame esta função e imprima o seu resultado.
"""
import psutil
        
def processos_caros(lst_processos, perc):
    
    # PARTE 1: obtém dados de todos os processos e média de gasto RSS
    soma_rss = 0
    tot_procs = 0
    lst_todos_processos = []
    lst_processos_caros = []
    
    for p in lst_processos:
        # e preciso usar o try, pois o processo pode ter saido da memória
        try:
            # pega os dados solicitados do processo e joga numa lista
            p = p.as_dict()
            p_pid = p['pid']
            p_nome = p['name']
            p_mem_rss = p['memory_info'].rss
            p_mem_vms = p['memory_info'].vms
            
            dic = {"pid": p_pid,
                   "nome": p_nome,
                   "mem_rss": p_mem_rss,
                   "mem_vms": p_mem_vms}
            
            lst_todos_processos.append(dic)
            
            #print(p_pid, p_nome, p_mem_rss, p_mem_vms)
            
            soma_rss  += p_mem_rss
            tot_procs += 1
            
        except:
            pass
        
    # PARTE 2: monta a lista de processos caros
    media_rss = soma_rss / tot_procs
    
    for p in lst_todos_processos:
        if p['mem_rss'] > media_rss + media_rss * perc/100:
            lst_processos_caros.append(p)
     
    
    #print(lst_todos_processos)
    
    return lst_processos_caros


for x in processos_caros(psutil.process_iter(), 70):
    print(x)