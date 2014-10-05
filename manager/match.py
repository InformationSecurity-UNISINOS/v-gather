#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import *
from base import *
from parser import *
from cqueue import *


'''
Similaridade:
Case-based reasoning is a methodology not a technology - I. Watson
AI-CBR, University of Salford, Salford M5 4WT, UK
Received 1 December 1998; accepted 17 March 1999

- Similarities are usually normalised to fall within a range of zero to one


Para as strings, usei Levenshtein, para números usei cosine similarity


http://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists
'''
def Similarity(item1,item2):
	import Levenshtein
	import math
	# SE É NUMERO
	if ( type(item1) == int or type(item1) == float ) and (type(item2) == int or type(item2) == float):
		a=item1*item1
		b=item2*item2
		if a < b:
			sim=round(a/math.sqrt(a*b),2)
		else:
			sim=round(b/math.sqrt(a*b),2)
	else:
		sim=round(Levenshtein.ratio(str(item1),str(item2)),2)
	return sim

def MatchData():
	print "[+] MatchData"
	debug=3

	sim_point=DbSimilarPoint()
	if sim_point == None:
		return False

	lista_casos=DbGetCaseID()
	for case_id in lista_casos:
		db_case={}
		db_case=DbGetCase(case_id)
		if db_case is 0 or db_case is False:
			return False
		print "lista_casos: "
		print lista_casos
		print "CASE ID: " + str(case_id)
		import sys
		sys.exit(1)
		
		db_so_name=DbGetSoName(db_case['so_id'])
		qlen=recvdata.LenQueue()
		while qlen>0:
			pdict = {}
			pdict = recvdata.GetQueue()
			scored = {}
			final_score=perfect=0

			#########################################################################
			# PAACKAGE MANAGER AND NAME
			#########################################################################
		
			p_pkg_ratio = Similarity( pdict['pacote'] , db_case['package_name'] )
			p_pkg_weight = float(db_case['package_name_weight'])
			p_pkg_score = float(p_pkg_ratio) * float(p_pkg_weight)
			
			final_score=final_score+p_pkg_score 
			if p_pkg_score == p_pkg_weight:
				perfect+=1
			#########################################################################
			# PROCESS PROCESS NAME
			#########################################################################
			p_name_ratio = Similarity( pdict['p_name'] , db_case['process_name'] )
			p_name_weight = float(db_case['process_name_weight'])
			p_name_score = float(p_name_ratio) * float(p_name_weight)
			final_score=final_score+p_name_score

			if p_name_score == p_name_weight:
				perfect+=1

			#########################################################################
			# PROCESS UID:
			#########################################################################
	 		p_uid_ratio = Similarity(pdict['p_uid'] , db_case['process_uid'])
	 		p_uid_weight = float(db_case['process_uid_weight'])
	 		p_uid_score = float(p_uid_weight) * float(p_uid_ratio)
	 		final_score=final_score+p_uid_score

	 		if p_uid_score == p_uid_weight:
	 			perfect+=1

			#########################################################################
			# PROCESS GID:
			#########################################################################
			p_gid_ratio = Similarity( pdict['p_gid'] , db_case['process_gid'])
			p_gid_weight = float(db_case['process_gid_weight'])
			p_gid_score = float(p_gid_ratio) * float(p_gid_weight)
			final_score=final_score+p_gid_score

			if p_gid_score == p_gid_weight:
				perfect+=1

			#########################################################################
			# PROCESS PROCESS ARGS
			#########################################################################
			p_args_ratio = Similarity(pdict['p_args'] ,db_case['process_args'])
			p_args_weight = float(db_case['process_args_weight'])
			p_args_score = float(p_args_ratio) * float(p_args_weight)
			final_score=final_score+p_args_score 

			if p_args_score == p_args_weight:
				perfect+=1

			#########################################################################
			# PROCESS TCP PORT AND BANNER (fromato: porta:banner)
			#########################################################################
			p_tcp_banner_ratio = Similarity( pdict['p_tcp_banner'] , db_case['process_tcp_banner'] )
			p_tcp_banner_weight = float(db_case['process_tcp_banner_weight'])
			p_tcp_banner_score = p_tcp_banner_ratio * p_tcp_banner_weight
			final_score=final_score+p_tcp_banner_score 

			if p_tcp_banner_score==p_tcp_banner_weight:
				perfect+=1

			#########################################################################
			# PROCESS UDP PORT AND BANNER (fromato: porta:banner)
			#########################################################################
			p_udp_banner_ratio = Similarity( pdict['p_udp_banner'] , db_case['process_udp_banner'] )
			p_udp_banner_weight = float(db_case['process_udp_banner_weight'])
			p_udp_banner_score = float(p_udp_banner_ratio) * float(p_udp_banner_weight)
			final_score=final_score+p_udp_banner_score 

			if p_udp_banner_score==p_udp_banner_weight:
				perfect+=1

			#########################################################################
			# PROCESS FILE PATH
			#########################################################################
			pf_path_ratio = Similarity( pdict['pf_path'] , db_case['process_binary'] )
			pf_path_weight = float(db_case['process_binary_weight'])
			pf_path_score = float(pf_path_ratio) * float(pf_path_weight)
			final_score=final_score+pf_path_score 

			if pf_path_score==pf_path_weight:
				perfect+=1

			#########################################################################
			# PROCESS DISTRO VERSION
			#########################################################################
			distro_version_ratio = Similarity(pdict['distro_version'], db_case['so_version'])
			distro_version_weight = float(db_case['so_version_weight'])
			distro_version_score = float(distro_version_ratio) * float(distro_version_weight)
			final_score=final_score+distro_version_score

			if distro_version_score==distro_version_weight:
				perfect+=1
			#########################################################################
			# PROCESS DISTRO NAME
			#########################################################################
			distro_ratio = Similarity( str(pdict['distro']) , str(db_so_name) )
			distro_weight = float(db_case['so_id_weight'])
 			distro_score = float(distro_ratio) * float(distro_weight)
 			final_score=final_score+distro_score

 			if distro_score== distro_weight:
 				perfect+=1

 			# so pra debug
 			#print pdict
 			#print "distro_score: " +str(distro_score)
 			#print "distro_version_score: " +str(distro_version_score)
 			#print "p_pkg_score: "+str(p_pkg_score)
 			#print "p_name_score: "+str(p_name_score)
 			#print "p_uid_score: "+str(p_uid_score)
 			#print "pf_path_score: " +str(pf_path_score)
 			#print "p_udp_banner_score: " +str(p_udp_banner_score)
 			#print "p_tcp_banner_score: " +str(p_tcp_banner_score)
 			#print "p_args_score: " +str(p_args_score)
 			#print "p_gid_score: " +str(p_gid_score)
 			
 			if debug==3:
				print "AG_PNAME: "+str(pdict['p_name']) + " / CASE_ID: " +str(case_id) + " / DB_PNAME: "+str( db_case['process_name']) + " / FINAL SCORE: " +str(final_score)
				print "*"*50

			if final_score > sim_point:
					scored['distro']=pdict['distro']
		 			scored['distro_weight']=float(distro_weight)
		 			scored['distro_score']=float(distro_score)
		 			scored['distro_version']=str(pdict['distro_version'])
					scored['distro_version_weight']=float(distro_version_weight)
					scored['distro_version_score']=float(distro_version_score)
		 			scored['p_name']=pdict['p_name']
					scored['p_name_weight']=float(p_name_weight)
					scored['p_name_score']=float(p_name_score)
					scored['p_uid']=int(pdict['p_uid'])
			 		scored['p_uid_weight']=float(p_uid_weight)
			 		scored['p_uid_score']=float(p_uid_score)
			 		scored['p_gid']=int(pdict['p_gid'])
			 		scored['p_gid_weight']=float(p_gid_weight)
			 		scored['p_gid_score']=float(p_gid_score)
			 		scored['p_args']= str(pdict['p_args'])
					scored['p_args_weight']=float(p_args_weight)
					scored['p_args_score']=float(p_args_score)
					scored['p_tcp_banner']=pdict['p_tcp_banner']
					scored['p_tcp_banner_weight']=float(p_tcp_banner_weight)
					scored['p_tcp_banner_score']=float(p_tcp_banner_score)
					scored['p_udp_banner'] = pdict['p_udp_banner']
					scored['p_udp_banner_weight']=float(p_udp_banner_weight)
					scored['p_udp_banner_score']=float(p_udp_banner_score)
					scored['p_package']=pdict['pacote']
					scored['p_pkg_weight']=float(p_pkg_weight)
					scored['p_pkg_score']=float(p_pkg_score)
					scored['pf_path'] = pdict['pf_path']
					scored['pf_path_weight']=float(pf_path_weight)
					scored['pf_path_score']=float(pf_path_score)
					scored['case_id_related']=case_id
					scored['score']=float(final_score)

					# A rotina abaixo utiliza o objeto filtro
					# para evitar que um dicionário igual (processo com todos os dados iguais)
					# seja cadastrado novamente
					flen=filtro.LenQueue()
					ja_cadastrado=False
					while flen>0:
						cadastrado = {}
						cadastrado = filtro.GetQueue()
						if cmp(cadastrado,scored) == 0:
							ja_cadastrado=True
							break
						flen-=1
					if ja_cadastrado==False:
						candidates.AddQueue(scored)
						filtro.AddQueue(scored)
					if perfect==10:
						break
			qlen-=1	
		case_id+=1
	recvdata.DestroyQueue()
	filtro.DestroyQueue()
	DbSimCases()
	return True








