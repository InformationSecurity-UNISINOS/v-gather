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

def SqlCountCases():
	conn=DbConnect()
	if conn == None:
		return False
	cursor = conn.cursor()
	case_sum="SELECT COUNT(id) from use_cases"
	cursor.execute (case_sum)
	result = cursor.fetchone()
	conn.close()
	return int(result[0])
	

def GetCase(case_id):
	conn=DbConnect()
	if conn == None:
		return False
	if SqlCountCases == 0:
		# nao existem casos na base
		return 0 
	cursor = conn.cursor()
	query="SELECT id,so_id,so_version,process_name,process_uid,process_gid,\
			process_tcp_banner,process_tcp_portcount,process_udp_banner,process_udp_portcount\
			process_args, \
			package_name,package_type_id,process_binary,process_binary_uid, \
			process_binary_gid,process_binary_dac \
			from use_cases where id=%i" %case_id 

	cursor.execute(query)
	results = cursor.fetchall()
	db_id=results[0][0]
	db_so_id=results[0][1]
	db_so_version=results[0][2]
	db_p_name=results[0][3]
	db_p_uid=results[0][4]
	db_p_gid=results[0][5]
	db_p_tcp_banner=results[0][6]
	db_p_tcp_portcount=results[0][7]
	db_p_udp_banner=results[0][8]
	db_p_udp_portcount=results[0][9]
	db_p_args=results[0][10]
	db_p_package=results[0][11]
	db_p_package_type_id=results[0][12]
	db_pf_path=results[0][13]
	db_pf_uid=results[0][14]
	db_pf_gid=results[0][15]
	db_pf_dac=results[0][16]

	print "*"*100
	print "[+] DATABASE VALUES:"
	print "  + CASO: " +str(db_id)
	print "  + SO: "+str(db_so_id)
	print "  + SO VER: " +str(db_so_version)
	print "  + PNAME: " +db_p_name
	print "  + PUID: " +str(db_p_uid)
	print "  + PGID: " +str(db_p_gid)
	print "  + TCP BANNER: "+db_p_tcp_banner
	print "  + TCP PORTS: "+str(db_p_tcp_portcount)
	print "  + UDP BANNER: "+str(db_p_udp_banner)
	print "  + UDP PORTCOUNT: "+str(db_p_udp_portcount)
	print "  + PARGS: "+db_p_args
	print "  + PKG: "+db_p_package
	print "  + PKG TYPE: "+str(db_p_package_type_id)
	print "  + PFPATH: " +db_pf_path
	print "  + PFUID: " +str(db_pf_uid)
	print "  + PFGID: " +str(db_pf_gid)
	print "  + PDAC: " +str(db_pf_dac)


def SqlQuery():
	
	
	cursor.execute ("select VERSION()")
	row = cursor.fetchone()
	print "Server version: ", row[0]
	cursor.close ()


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
def SqlQueryAll():
	conn = MySQLdb.connect (host = sqlhost, user = sqluser, passwd = sqlpass, db = sqldb)
	cursor = conn.cursor()
	sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()
		for row in results:
			fname = row[0]
	      	lname = row[1]
	      	age = row[2]
	      	sex = row[3]
	      	income = row[4]
	      	# Now print fetched result
	      	print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
	             (fname, lname, age, sex, income )
		except:
	   		print "Error: unable to fecth data"
	  	conn.close ()












