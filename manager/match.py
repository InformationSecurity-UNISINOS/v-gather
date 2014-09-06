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

			debug=1
			if debug==1:
				print "[+] RATIO"
				print "  + SO NAME: " + qitem['distro'] + " ratio: "+str(so_name_ratio)
				print "  + SO VER: " + qitem['distro_version']+ " ratio: "+str(so_version_ratio)
				print "  + P NAME: " + qitem['p_name'] +" ratio: "+str(p_name_ratio)
				print "  + P UID: " + str(qitem['p_uid'])+" ratio: "+str(p_uid_ratio)
				print "  + P GID: " + str(qitem['p_gid'])+" ratio: "+str(p_gid_ratio)
				print "  + P ARGS: " + qitem['p_args']+" ratio: "+str(p_args_ratio)
				print "  + TCP BANNER: " +qitem['p_tcp_banner'] + " ratio: "+str(p_tcp_banner_ratio)
				print "  + TCP COUNT: " + str(qitem['p_tcp_portcount'])+" ratio: "+str(p_tcp_portcount_ratio)
				print "  + UDP BANNER: " + qitem['p_udp_banner']+" ratio: "+str(p_udp_banner_ratio)
				print "  + UDP PORTCOUNT: " + str(qitem['p_udp_portcount'])+" ratio: "+str(p_udp_portcount_ratio)
				print "  + PKG MGR: " +str(p_pkgmgr_ratio)
				print "  + PKG: "  +str(p_pkg_ratio)
				print "  + FILE PATH: " + qitem['pf_path']+" ratio: "+str(pf_path_ratio)
				print "  + FILE UID: " + str(qitem['pf_uid'])+ " ratio: "+str(pf_uid_ratio)
				print "  + FILE GID: " + str(qitem['pf_gid'])+" ratio: "+str(pf_gid_ratio)
				print "  + FILE DAC: " + str(qitem['pf_dac'])+" ratio: "+str(pf_dac_ratio)

			qlen-=1
		case_id+=1
	DestroyQueue()




