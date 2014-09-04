#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
'''
O server abre o listener e chama o rpc pra receber os dados.
o rpc recebe os dados do agente e joga pro queue organizar tudo em uma fila de dicionários (um dicionário por processo)
Quando os dados estiverem organizados, o queue.py deve retornar a fila(queue) para o rpc.
O rpc vai receber os dados tratados e encaminhar para o core.py

O core.py vai solicitar para o base.py um caso usando um index (case_id) incremental, via laço for.
o base.py vai pesquisar no MySQL o caso com o case_id solicitado pelo core.py e devolver um dicionário.
O core.py terá na mão o caso da base e a lista de dicionários recebida através do rpc.py
o core.py vai então encaminhar os pares de casos (base e dado do agente) pro match.py

O match.py vai recever dois dicionários do core.py, e calcular a similaridade dos atributos entre o caso da base e o dado do agente.

O estado (dado do agente) que tiver mais que <60%> de similaridade com algum caso da base, será adicionado a uma nova lista de dicionários.
Quando todos os estados (dado do agente) forem comparados com todos os itens da base, a lista de dicionário final (passo anterior),
será enviada para o base.py

O base.py vai receber a lista de casos que devem ser adaptados, e inserir no MySQL com status '2'.

No front-end, os itens da base com status '2' devem ser exibidos em pares:
ESTADO COLETADO DO AGENTE X CASO DA BASE SEMELHANTE 
O usuário deverá selecionar se ele quer aplicar a solução do caso da base, no estado coletado. Ou será necessário adaptar.
Caso o usuário entenda que é melhor adaptar, ele deverá editar o campo solução e poderá adicionar descrição.

Quando ele salvar esse resultado, o status no mysql deve ser alterado pra 1, e a data deve ser inserida.
Talvez seja interessante colocar uma outra flag pra determinar que este foi um caso APRENDIDO.

A lista de todos os casos já está disponível no frontend

'''
from collections import deque
pqueue = deque()

def GetQueue():
	 return pqueue.popleft()

def AddQueue(dict={}):
	pqueue.append(dict)
                