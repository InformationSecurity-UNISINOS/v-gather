<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start(); 
if(login_check($mysqli) == false) {

        header('Location: index.php');
}

$row_id=$_REQUEST['field'];
echo $row_id;
die();
$stmt2 = $mysqli->prepare("UPDATE use_cases SET status=3 WHERE id = ?");
$stmt2->bind_param('i', $row_id);
$stmt2->execute(); 
$stmt2->free_result();
$stmt2->close();

header('Location: matching.php');

?>