#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import MySQLdb
from common import *

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



def DbSimCases():
	clen=candidates.LenQueue()
	while clen > 0:
		proc=candidates.GetQueue()
		for key, value in proc.iteritems():
			print "%s: %s" %(key,value)
			print "*"*50
		clen-=1
	candidates.DestroyQueue()
	#conn = MySQLdb.connect (host = sqlhost, user = sqluser, passwd = sqlpass, db = sqldb)
	#cursor = conn.cursor()
	#sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) \
    #   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
    #   ('Mac', 'Mohan', 20, 'M', 2000)
	#try:
#		cursor.execute(sql)
 #  		conn.commit()
#	except:
 #  		# Rollback in case there is any error
  # 		conn.rollback()
   #	conn.close ()





