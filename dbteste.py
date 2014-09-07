import MySQLdb

sqlhost="127.0.0.1" 
sqluser="vmgr"
sqlpass="teste"
sqldb="vgather"

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
	query="SELECT so_id,so_version,process_name,process_uid,process_gid,\
			process_tcp_banner,process_tcp_portcount,process_udp_banner,process_udp_portcount\
			process_args, \
			package_name,package_type_id,process_binary,process_binary_uid, \
			process_binary_gid,process_binary_dac \
			from use_cases where id=1" 

	cursor.execute(query)
	results = cursor.fetchall()
	db_id=results[0][0]
	db_version=results[0][1]
	db_p_name=results[0][2]
	db_p_uid=results[0][3]
	db_p_gid=results[0][4]
	db_p_tcp_banner=results[0][5]
	db_p_tcp_portcount=results[0][6]
	db_p_udp_banner=results[0][7]
	db_p_udp_portcount=results[0][8]
	db_p_args=results[0][9]
	db_p_package=results[0][10]
	db_p_package_type_id=results[0][11]
	db_pf_path=results[0][12]
	db_pf_uid=results[0][13]
	db_pf_gid=results[0][14]
	db_pf_dac=results[0][15]


SqlCountCases()
