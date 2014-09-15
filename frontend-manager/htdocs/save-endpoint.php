<?php
	include_once 'includes/db_connect.php';
	include_once 'includes/functions.php';
	sec_session_start(); 
	if(login_check($mysqli) == false) {

	        header('Location: index.php');
	}


	if ( isset($_POST['new_ag_hostname']) && isset($_POST['new_ag_ipaddr']) ) {
		$new_ag_ipaddr=$_POST['new_ag_ipaddr'];
		$new_ag_hostname=$_POST['new_ag_hostname'];
		include_once 'includes/db_connect.php';
		include_once 'includes/functions.php';
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