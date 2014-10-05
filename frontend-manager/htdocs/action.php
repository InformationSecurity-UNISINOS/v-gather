<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start(); 
if(login_check($mysqli) == false) {

        header('Location: index.php');
}

if ( $_GET['mode'] == "reject" ) {
	if (isset($_GET['field'])) { 
		$row_id=$_GET['field'];
		$stmt2 = $mysqli->prepare("DELETE FROM use_cases WHERE id = ?");
		$stmt2->bind_param('i', $row_id);
		$stmt2->execute(); 
		$stmt2->free_result();
		$stmt2->close();
		header('Location: matching.php');
	}
}

if ( $_GET['mode'] == "evaluate" ) {
	if ( isset($_GET['field']) ) { 
		$row_id=$_REQUEST['field'];
		$stmt2 = $mysqli->prepare("UPDATE use_cases SET status=3 WHERE id = ?");
		$stmt2->bind_param('i', $row_id);
		$stmt2->execute(); 
		$stmt2->free_result();
		$stmt2->close();
		header('Location: matching.php');
	}
}

if ( $_GET['mode'] == "perfect" ) {
	if ( isset($_GET['field']) ) { 
		$row_id=$_REQUEST['field'];
		$stmt2 = $mysqli->prepare("UPDATE use_cases SET status=1 WHERE id = ?");
		$stmt2->bind_param('i', $row_id);
		$stmt2->execute(); 
		$stmt2->free_result();
		$stmt2->close();
		header('Location: evaluate.php');
	}
}

if ( $_GET['mode'] == "endpoint" ) {
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
		header('Location: endpoints.php');
	}
}


if ( $_GET['mode'] == "settings" ) {
	if ( isset($_POST['novo_valor']) AND isset($_POST['nova_desc']) AND isset($_POST['tupla']) ) {
		$valor=xss_clean($_POST['novo_valor']);
		$descricao=xss_clean($_POST['nova_desc']);
		$id=$_POST['tupla'];

		$stmt=$mysqli->prepare("UPDATE weight_settings SET weight=?, descr=? WHERE id=?");
		if ($stmt === FALSE) {
		    die ("Mysql Error 1: " . $mysqli->error);
		}

		$stmt->bind_param('ssi', $valor,$descricao,$id );
		$stmt->execute();
		$stmt->free_result();

		header('Location: settings.php');
	}
}


?>