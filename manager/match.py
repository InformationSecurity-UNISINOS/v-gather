#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import *
from base import *
from cqueue import*

def Similarity(string_a,string_b):
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
    return fuzz.ratio(string_a,string_b)


def MatchData():

	# quantos casos tem na base?
	total_cases=DbCountCases()
	if total_cases == False:
		return False
	# ok, criar loop pra recuberar cada caso da base
	case_id=1
	qlen=LenQueue()
	while case_id <= total_cases:
		db_case={}
		db_case=DbGetCase(case_id)
		while qlen >0:
			qitem=GetQueue()
			db_so_name=DbGetSoName(db_case['so_id'])
			db_pkg_mgr=DbGetPkgMgr(db_case['package_type_id'])
			

			so_name_ratio=Similarity(db_so_name,qitem['distro'])	
			so_version_ratio=Similarity(db_case['so_version'],qitem['distro_version'])	
			p_name_ratio=Similarity(db_case['p_name'],qitem['p_name'])					
			p_uid_ratio=Similarity(db_case['p_uid'],qitem['p_uid'])				
			p_gid_ratio=Similarity(db_case['p_gid'],qitem['p_gid'])							 
			p_args_ratio=Similarity(db_case['p_args'],qitem['p_args'])								
			p_tcp_banner_ratio=Similarity(db_case['p_tcp_banner'],qitem['p_tcp_banner'])			
			p_tcp_portcount_ratio=Similarity(db_case['p_tcp_portcount'],qitem['p_tcp_portcount'])	
			p_udp_banner_ratio=Similarity(db_case['p_udp_banner'],qitem['p_udp_banner'])	
			p_udp_portcount_ratio=Similarity(db_case['p_udp_portcount'],qitem['p_udp_portcount'])	

			if qitem['p_dpkg'] is not None and qitem['p_dpkg'] is not '':					
 				q_pkg_type="DPKG"	
 				p_pkgmgr_ratio=Similarity(db_pkg_mgr,q_pkg_type)														
				p_pkg_ratio=Similarity(db_case['package'],qitem['p_dpkg'])								
			else:																			
				q_pkg_type="RPM"															
				p_pkg_ratio=Similarity(db_case['package'],qitem['p_rpm'])
			p_pkgmgr_ratio=Similarity(db_pkg_mgr,q_pkg_type)							
			pf_path_ratio=Similarity(db_case['pf_path'],qitem['pf_path'])
			pf_uid_ratio=Similarity(db_case['pf_uid'],qitem['pf_uid'])
			pf_gid_ratio=Similarity(db_case['pf_gid'],qitem['pf_gid'])
			pf_dac_ratio=Similarity(db_case['pf_dac'],qitem['pf_dac'])

			debug=0
			if debug==1:
				print "[+] RATIO"
				print "  + SO NAME: " +str(so_name_ratio)
				print "  + SO VER: " +str(so_version_ratio)
				print "  + P NAME: " +str(p_name_ratio)
				print "  + P UID: " +str(p_uid_ratio)
				print "  + P GID: " +str(p_gid_ratio)
				print "  + P ARGS: " +str(p_args_ratio)
				print "  + TCP BANNER: " +str(p_tcp_banner_ratio)
				print "  + TCP COUNT: " +str(p_tcp_portcount_ratio)
				print "  + UDP BANNER: " +str(p_udp_banner_ratio)
				print "  + UDP PORTCOUNT: " +str(p_udp_portcount_ratio)
				print "  + PKG MGR: " +str(p_pkgmgr_ratio)
				print "  + PKG: " +str(p_pkg_ratio)
				print "  + FILE PATH: " +str(pf_path_ratio)
				print "  + FILE UID: " +str(pf_uid_ratio)
				print "  + FILE GID: " +str(pf_gid_ratio)
				print "  + FILE DAC: " +str(pf_dac_ratio)

			

			qlen-=1
		case_id+=1
	DestroyQueue()




