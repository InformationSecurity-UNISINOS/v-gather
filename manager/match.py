#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import *
from base import *
from parser import *
from cqueue import * 

def Similarity(string_a,string_b):
	import Levenshtein
	return round(Levenshtein.ratio(string_a,string_b),2)


def MatchData():
	
	print "[+] MatchData"

	total_cases=DbCountCases()
	if total_cases == False:
		return False
	case_id=1
	while case_id <= total_cases:
		db_case={}
		db_case=DbGetCase(case_id)
		if db_case is 0 or db_case is False:
			return False
		db_so_name=DbGetSoName(db_case['so_id'])
		db_pkg_mgr=DbGetPkgMgr(db_case['package_type_id'])
		debug=True

		qlen=LenQueue()
		while qlen>0:
			print "*"*20
			pdict = GetQueue()
			#########################################################################
			# PAACKAGE MANAGER AND NAME
			#########################################################################
			if pdict['p_dpkg']:
				p_pkgm_ratio = Similarity( pdict['p_dpkg'] , db_pkg_mgr )
				p_pkg_ratio = Similarity( pdict['p_dpkg'] , db_case['package_name'] )
			if pdict['p_rpm']:
				p_pkgm_ratio = Similarity( pdict['p_rpm'] , db_pkg_mgr )
				p_pkg_ratio = Similarity( pdict['p_rpm'] , db_case['package_name'] )
			p_pkg_weight = db_case['package_name_weight']
			p_pkg_score = p_pkg_ratio * p_pkg_weight
			p_pkgm_weight = db_case['package_type_id_weight']
			p_pkgm_score = p_pkg_weight * p_pkg_ratio
			if debug==True:
				print "*"*100
				print "Gerenciador de Pacotes: %s" +str(p_pkgm_ratio)
				print "Peso: %s" +str(p_pkgm_weight)
				print "Score: %s" +str(p_pkg_score)
				print "*"*100
				print "Pacote: %s" +str(p_pkg_ratio)
				print "Peso: %s" +str(p_pkg_weight)
				print "Score: %s" +str(p_pkg_score)
				
			#########################################################################
			# PROCESS PROCESS NAME
			#########################################################################
			p_name_ratio = Similarity( pdict['p_name'] , db_case['process_name'] )
			p_name_weight = db_case['process_name_weight']
			p_name_score = p_name_ratio * p_name_weight
			if debug==True:
				print "*"*100
				print "Processo: %s" +str(p_name_ratio)
				print "Peso: %s" +str(p_name_weight)
				print "Score: %s" +str(p_name_score)
			#########################################################################
			# PROCESS UID:
			#########################################################################
	 		p_uid_ratio = Similarity( pdict['p_uid'] , db_case['process_uid'] )
	 		p_uid_weight = db_case['process_uid_weight']
	 		p_uid_score = p_uid_weight * p_uid_ratio
	 		if debug==True:
				print "*"*100
				print "P UID: %s" +str(p_uid_ratio)
				print "Peso: %s" +str(p_uid_weight)
				print "Score: %s" +str(p_uid_score)
			#########################################################################
			# PROCESS GID:
			#########################################################################
			p_gid_ratio = Similarity( pdict['p_gid'] , db_case['process_gid'] )
			p_gid_weight = db_case['process_gid_weight']
			p_gid_score = p_gid_ratio * p_gid_weight
			if debug==True:
				print "*"*100
				print "P GID: %s" +str(p_gid_ratio)
				print "Peso: %s" +str(p_gid_weight)
				print "Score: %s" +str(p_gid_score)
			#########################################################################
			# PROCESS PROCESS ARGS
			#########################################################################
			p_args_ratio = Similarity( pdict['p_args'] , db_case['process_args'] )
			p_args_weight = b_case['process_args_weight']
			p_args_score = p_args_ratio * p_args_weight
			if debug==True:
				print "*"*100
				print "P ARGS: %s" +str(p_args_ratio)
				print "Peso: %s" +str(p_args_weight)
				print "Score: %s" +str(p_args_score)
			#########################################################################
			# PROCESS TCP PORT AND BANNER (fromato: porta:banner)
			#########################################################################
			p_tcp_banner_ratio = Similarity( pdict['p_tcp_banner'] , db_case['process_tcp_banner'] )
			p_tcp_banner_weight = db_case['process_tcp_banner_weight']
			p_tcp_banner_score = p_tcp_banner_ratio * p_tcp_banner_weight
			if debug==True:
				print "*"*100
				print "P TCP BANNER: %s" +str(p_tcp_banner_ratio)
				print "Peso: %s" +str(p_tcp_banner_weight)
				print "Score: %s" +str(p_tcp_banner_score)
			#########################################################################
			# PROCESS UDP PORT AND BANNER (fromato: porta:banner)
			#########################################################################
			p_udp_banner_ratio = Similarity( pdict['p_udp_banner'] , db_case['process_udp_banner'] )
			p_udp_banner_weight = db_case['process_udp_banner_weight']
			p_udp_banner_score = p_udp_banner_ratio * p_udp_banner_weight
			if debug==True:
				print "*"*100
				print "P UDP BANNER: %s" +str(p_udp_banner_ratio)
				print "Peso: %s" +str(p_udp_banner_weight)
				print "Score: %s" +str(p_udp_banner_score)
			#########################################################################
			# PROCESS FILE PATH
			#########################################################################
			pf_path_ratio = Similarity( pdict['pf_path'] , db_case['process_binary'] )
			pf_path_weight = db_case['process_binary_weight']
			pf_path_score = pf_path_ratio * pf_path_weight
			if debug==True:
				print "*"*100
				print "PF PATH: %s" +str(pf_path_ratio)
				print "Peso: %s" +str(pf_path_weight)
				print "Score: %s" +str(pf_path_score)
			#########################################################################
			# PROCESS FILE UID OWNER
			#########################################################################
			pf_uid_ratio = Similarity( pdict['pf_uid'] , db_case['process_binary_uid'] )
			pf_uid_weight = db_case['process_binary_uid_weight']
			pf_uid_score = pf_uid_ratio * pf_uid_weight
			if debug==True:
				print "*"*100
				print "PF UID: %s" +str(pf_uid_ratio)
				print "Peso: %s" +str(pf_uid_weight)
				print "Score: %s" +str(pf_uid_score)
			#########################################################################
			# PROCESS FILE GID OWNER
			#########################################################################
			pf_gid_ratio = Similarity( pdict['pf_gid'] , db_case['process_binary_gid'] )
			pf_gid_weight = db_case['process_binary_gid_weight']
			pf_gid_score = pf_gid_ratio * pf_gid_weight
			if debug==True:
				print "*"*100
				print "PF GID: %s" +str(pf_gid_ratio)
				print "Peso: %s" +str(pf_gid_weight)
				print "Score: %s" +str(pf_gid_score)
			#########################################################################
			# PROCESS FILE DAC
			#########################################################################
			pf_dac_ratio = Similarity( pdict['pf_dac'] ,  db_case['process_binary_dac'] )
			pf_dac_weight = db_case['process_binary_dac_weight']
			pf_dac_score = pf_dac_ratio * pf_dac_weight
			if debug==True:
				print "*"*100
				print "PF DAC: %s" +str(pf_dac_ratio)
				print "Peso: %s" +str(pf_dac_weight)
				print "Score: %s" +str(pf_dac_score)
			#########################################################################
			# PROCESS DISTRO VERSION
			#########################################################################
			distro_version_ratio = Similarity( pdict['distro_version'] ,  db_case['so_version'] )
			distro_version_weight = db_case['so_version_weight']
			distro_version_score = distro_version_ratio * distro_version_weight
			if debug==True:
				print "*"*100
				print "DISTRO VERSION: %s" +str(distro_version_ratio)
				print "Peso: %s" +str(distro_version_weight)
				print "Score: %s" +str(distro_version_score)
			#########################################################################
			# PROCESS DISTRO NAME
			#########################################################################
			distro_ratio = Similarity( pdict['distro'] , db_so_name )
			distro_weight = db_case['so_id_weight']
 			distro_score = distro_ratio * distro_weight
			if debug==True:
				print "*"*100
				print "DISTRO NAME: %s" +str(distro_ratio)
				print "Peso: %s" +str(distro_weight)
				print "Score: %s" +str(distro_score)
				
			qlen-=1				
			print "*"*100
		case_id+=
	DestroyQueue()		
		return True



