<?php
	include_once 'includes/db_connect.php';
	include_once 'includes/functions.php';
	include_once 'inclides/xss_clean.php';
	sec_session_start(); 
	if(login_check($mysqli) == false) {

	        header('Location: index.php');
	}


	if ( isset($_POST['new_ag_hostname']) && isset($_POST['new_ag_ipaddr']) ) {
		$new_ag_ipaddr=xss_clean($_POST['new_ag_ipaddr']);
		$new_ag_hostname=xss_clean($_POST['new_ag_hostname']);

		$stmt=$mysqli->prepare("INSERT INTO managed_servers (ipaddress,hostname,created,updated)
		VALUES(?,?,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)");
		if ($stmt === FALSE) {
			die ("Mysql Error 1: " . $mysqli->error);
		}
		$stmt->bind_param('ss',$new_ag_ipaddr,$new_ag_hostname);
		$stmt->execute();
		$stmt->free_result();
		$stmt->close();
		
	}
	header('Location: endpoints.php');
?>