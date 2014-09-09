#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import *
from base import *
from parser import *
from cqueue import * 

def Similarity(string_a,string_b):
	from difflib import SequenceMatcher
	return round(SequenceMatcher(None, string_a,string_b).ratio(),2)


def MatchData():
	Debug=1
	# quantos casos tem na base?
	total_cases=DbCountCases()
	if total_cases == False:
		return False
	# ok, criar loop pra recuberar cada caso da base
	case_id=1
	qlen=LenQueue()
	if Debug==1:
		while qlen>0:
			pdict = GetQueue()
			for key in pdict.iterkeys():
				val1, val2 = map(float, pdict[key])
				print "%s: %s" %(str(val1),str(val2))
			qlen-=1
	DestroyQueue()		#remover - debug
	return 1			#remover - debug


#	while case_id <= total_cases:
#		db_case={}
#		db_case=DbGetCase(case_id)
#		while qlen >0:
#			qitem=GetQueue()
#			db_so_name=DbGetSoName(db_case['so_id'])
#			db_pkg_mgr=DbGetPkgMgr(db_case['package_type_id'])



			'''
			db_case['case_id']
			db_case['so_id_weight']
			db_case['so_version']
			db_case['so_version_weight']
			db_case['process_name']
			db_case['process_name_weight']
			db_case['process_uid']
			db_case['process_uid_weight']
			db_case['process_gid']
			db_case['process_gid_weight']
			db_case['process_args']
			db_case['process_args_weight']
			db_case['process_tcp_banner']
			db_case['process_tcp_banner_weight']
			db_case['process_udp_banner']
			db_case['rocess_udp_banner_weight']
			db_case['process_tcp_portas']
			db_case['process_tcp_portas_weight']
			db_case['process_udp_portas']
			db_case['process_udp_portas_weight']
			db_case['package_name']
			db_case['package_name_weight']
			db_case['package_type_id']
			db_case['package_type_id_weight']
			db_case['process_binary']
			db_case['process_binary_weight']
			db_case['process_binary_dac']
			db_case['process_binary_dac_weight']
			db_case['process_binary_uid']
			db_case['process_binary_uid_weight']
			db_case['process_binary_gid']
			db_case['process_binary_gid_weight']
			'''



#			qlen-=1
#		case_id+=1
#	DestroyQueue()




