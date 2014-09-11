#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
'''
O server abre o listener e chama o rpc pra receber os dados.
o rpc recebe os dados do agente e joga pro queue organizar tudo em uma fila de dicionários (um dicionário por processo)
Quando os dados estiverem organizados, o queue.py deve retornar a lista para o rpc.
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
import MySQLdb
from common import *

def DbConnect():
	try:
		ret=MySQLdb.connect(host=sqlhost, user=sqluser, passwd=sqlpass, db=sqldb)
	except:
		ret=None
	return ret

def DbCountCases():
	conn=DbConnect()
	if conn == None:
		return False
	cursor = conn.cursor()
	case_sum="SELECT COUNT(id) from use_cases"
	cursor.execute (case_sum)
	result = cursor.fetchone()
	conn.close()
	return int(result[0])


def DbCheckAgent(agent_addr):
	conn=DbConnect()
	if conn == None:
		return False
	cursor = conn.cursor()
	ipaddr="SELECT id from managed_servers WHERE ipaddress like '%s'" %agent_addr
	cursor.execute (ipaddr)
	result = cursor.fetchone()
	conn.close()
	try:
		if int(result[0]) >0:
			return True
	except:
		return False

def DbGetCase(case_id):
	conn=DbConnect()
	if conn == None:
		return False
	if DbCountCases() == 0:
		# nao existem casos na base
		return 0 
	cursor = conn.cursor()
	query="SELECT id,\
	so_id, so_id_weight, \
	so_version, so_version_weight,\
	process_name, process_name_weight,\
	process_uid, process_uid_weight,\
	process_gid, process_gid_weight,\
	process_args, process_args_weight,\
	process_tcp_banner, process_tcp_banner_weight,\
	process_udp_banner, process_udp_banner_weight,\
	process_tcp_portas, process_tcp_portas_weight,\
	process_udp_portas, process_udp_portas_weight, \
	package_name, package_name_weight,\
	package_type_id, package_type_id_weight,\
	process_binary, process_binary_weight,\
	process_binary_dac, process_binary_dac_weight,\
	process_binary_uid, process_binary_uid_weight,\
	process_binary_gid, process_binary_gid_weight\
	from use_cases where id=%i" %case_id 

	cursor.execute(query)
	results = cursor.fetchall()
	db_case={}
	db_case['case_id']=results[0][0]
	db_case['so_id']=results[0][1]
	db_case['so_id_weight']=results[0][2]
	db_case['so_version']=results[0][3]
	db_case['so_version_weight']=results[0][4]
	db_case['process_name']=results[0][5]
	db_case['process_name_weight']=results[0][6]
	db_case['process_uid']=results[0][7]
	db_case['process_uid_weight']=results[0][8]
	db_case['process_gid']=results[0][9]
	db_case['process_gid_weight']=results[0][10]
	db_case['process_args']=results[0][11]
	db_case['process_args_weight']=results[0][12]
	db_case['process_tcp_banner']=results[0][13]
	db_case['process_tcp_banner_weight']=results[0][14]
	db_case['process_udp_banner']=results[0][15]
	db_case['process_udp_banner_weight']=results[0][16]
	db_case['process_tcp_portas']=results[0][17]
	db_case['process_tcp_portas_weight']=results[0][18]
	db_case['process_udp_portas']=results[0][19]
	db_case['process_udp_portas_weight']=results[0][20]
	db_case['package_name']=results[0][21]
	db_case['package_name_weight']=results[0][22]
	db_case['package_type_id']=results[0][23]
	db_case['package_type_id_weight']=results[0][24]
	db_case['process_binary']=results[0][25]
	db_case['process_binary_weight']=results[0][26]
	db_case['process_binary_dac']=results[0][27]
	db_case['process_binary_dac_weight']=results[0][28]
	db_case['process_binary_uid']=results[0][29]
	db_case['process_binary_uid_weight']=results[0][30]
	db_case['process_binary_gid']=results[0][31]
	db_case['process_binary_gid_weight']=results[0][32]
	conn.close()
	return db_case
	
def DbGetPkgMgr(package_type_id):
	conn=DbConnect()
	if conn == None:
		return False
	if DbCountCases == 0:
		# nao existem casos na base
		return 0 
	cursor = conn.cursor()
	query="Select name from package_types where id=%i" %int(package_type_id)
	cursor.execute(query)
	results = cursor.fetchone()
	conn.close()
	return results[0]

def DbGetSoName(so_id):
	conn=DbConnect()
	if conn == None:
		return False
	if DbCountCases == 0:
		# nao existem casos na base
		return 0 
	cursor = conn.cursor()
	query="Select name from sos where id=%i" %int(so_id)
	cursor.execute(query)
	results = cursor.fetchone()
	conn.close()
	return results[0]



def SqlInsert():
	conn = MySQLdb.connect (host = sqlhost, user = sqluser, passwd = sqlpass, db = sqldb)
	cursor = conn.cursor()
	sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
	try:
		cursor.execute(sql)
   		conn.commit()
	except:
   		# Rollback in case there is any error
   		conn.rollback()
   	conn.close ()





