#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# A organização dos casos funciona no esquema
# 2.5.1.1 Memória linear com busca serial (dumbo)
#
# A adaptação da solução será baseada em crítica.
# O usuário vai observar a solução e fazer a adaptação manualmente, caso seja necessário.
# Caso não seja necessário, a adaptação nula é adotada (apenas aplica como está)
#
#
#
#


import MySQLdb
from common import *
from cqueue import *

def DbConnect():
	try:
		ret=MySQLdb.connect(host=sqlhost, port=3306, user=sqluser, passwd=sqlpass, db=sqldb)
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

def DbSimilarPoint():
	conn=DbConnect()
	if conn == None:
		return False
	cursor = conn.cursor()
	decpoint="SELECT value FROM case_match"
	cursor.execute (decpoint)
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
	db_case['package_name']=results[0][17]
	db_case['package_name_weight']=results[0][18]
	db_case['package_type_id']=results[0][19]
	db_case['package_type_id_weight']=results[0][20]
	db_case['process_binary']=results[0][21]
	db_case['process_binary_weight']=results[0][22]
	db_case['process_binary_dac']=results[0][23]
	db_case['process_binary_dac_weight']=results[0][24]
	db_case['process_binary_uid']=results[0][25]
	db_case['process_binary_uid_weight']=results[0][26]
	db_case['process_binary_gid']=results[0][27]
	db_case['process_binary_gid_weight']=results[0][28]
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
#
# Eu havia criado uma classe de fila
# pra instanciar filas como objetos.
# O problema é que quando eu alimentava os valores da 
# fila filtrada (a ser inserida na base),
# os valores float nos scores eram totalmente modificados.
# valor que deveria ser 3.0, estava como 0.45.
# nao consegui resolver esse problema, nao encontrei a causa raíz.
# fiquei um dia inteiro em cima desse problema e nada.
# pra evitar perder tanto tempo, mudei a abordagem
# ao invés de usar uma queue de dados pra inserir na base
# mandei inserir diretamente, sem queue.
# vai diminuir a performance, mas ...
def DbSimCases():
	#clen=candidates.LenQueue()
	clen=LenQueue(can_queue)

	while clen > 0:
		pdict2={}
		#pdict2=candidates.GetQueue()
		pdict2=GetQueue(can_queue)
		if pdict2['distro'] == "Debian":
			so_id=1
		else: 
			so_id=2
		if pdict2['p_dpkg']:
			package_name=pdict2['p_dpkg']
			package_manager=1
		else:
			package_name=pdict2['p_rpm']
			package_manager=2

		# noarmalizando dados,
		# antes de inserir na base:

		print "*"*50
		for k,v in pdict2.items():
			if v == "" or len(str(v)) == 0:
				pdict2[k]=None
			print "%s: %s" %(k,v)
		print "*"*50
		
		clen-=1

		conn=DbConnect()
		if conn == None:
			return False
		cursor = conn.cursor()

		query = "INSERT INTO use_cases ( status, origem, case_id_related, \
										so_id, so_id_weight, so_id_score, \
										so_version, so_version_weight, so_version_score, \
										process_name, process_name_weight, process_name_score, \
										process_uid, process_uid_weight, process_uid_score, \
										process_gid, process_gid_weight, process_gid_score, \
										process_args, process_args_weight, process_args_score, \
										process_tcp_banner, process_tcp_banner_weight, process_tcp_banner_score, \
										process_udp_banner, process_udp_banner_weight, process_udp_banner_score, \
										package_name, package_name_weight, package_name_score, \
										package_type_id, package_type_id_weight, package_type_id_score, \
										process_binary, process_binary_weight, process_binary_score, \
										process_binary_uid, process_binary_uid_weight, process_binary_uid_score, \
										process_binary_gid, process_binary_gid_weight, process_binary_gid_score, \
										process_binary_dac, process_binary_dac_weight, process_binary_dac_score, \
										candidate_final_score) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s" )" % ( 2, 2, str(pdict2['case_id_related']),str(so_id), str(pdict2['distro_weight']), str(pdict2['distro_score']), str(pdict2['distro_version']), str(pdict2['distro_version_weight']), str(pdict2['distro_version_score']), str(pdict2['p_name']),str(pdict2['p_name_weight']), str(pdict2['p_name_score']), str(pdict2['p_uid']), str(pdict2['p_uid_weight']), str(pdict2['p_uid_score']), str(pdict2['p_gid']), str(pdict2['p_gid_weight']), str(pdict2['p_gid_score']), str(pdict2['p_args']),str(pdict2['p_args_weight']), str(pdict2['p_args_score']), str(pdict2['p_tcp_banner']), str(pdict2['p_tcp_banner_weight']), str(pdict2['p_tcp_banner_score']), str(pdict2['p_udp_banner']), str(pdict2['p_udp_banner_weight']), str(pdict2['p_udp_banner_score']), str(package_name), str(pdict2['p_pkg_weight']), str(pdict2['p_pkg_score']), str(package_manager), str(pdict2['p_pkgmgr_weight']), str(pdict2['p_pkgmgr_score']), str(pdict2['pf_path']), str(pdict2['pf_path_weight']), str(pdict2['pf_path_score']), str(pdict2['pf_uid']), str(pdict2['pf_uid_weight']), str(pdict2['pf_uid_score']), str(pdict2['pf_gid']), str(pdict2['pf_gid_weight']), str(pdict2['pf_gid_score']), str(pdict2['pf_dac']), str(pdict2['pf_dac_weight']), str(pdict2['pf_dac_score']), str(pdict2['score']) )
		cursor.execute(query)
		conn.commit()
		conn.close ()
		clen-=1

	candidates.DestroyQueue()





