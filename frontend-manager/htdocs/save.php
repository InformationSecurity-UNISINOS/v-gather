<html>
<body>


<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start(); 
if(login_check($mysqli) == false) {
	die('Você precisa se autenticar para acessar esta página.');
}

if (isset($_POST['so'])) {
	if ($_POST['so'] == "debian") {
    $so_id=1;
  }
  if ($_POST['so'] == "centos") {
    $so_id=2;
  }
}
if (isset($_POST['so_weight'])) {
  $so_weight=$_POST['so_weight'];
}
//============================================================================================================

if (isset($_POST['so_ver'])) {
    $so_ver=$_POST['so_ver'];
}
if (isset($_POST['so_ver_weight'])) {
  $so_ver_weight=$_POST['so_ver_weight'];
}
//============================================================================================================

if (isset($_POST['p_name'])) {
	$p_name=$_POST['p_name'];
}
if (isset($_POST['p_name_weight'])) {
  $p_name_weight=$_POST['p_name_weight'];
}
//============================================================================================================

if (isset($_POST['p_uid'])) {
	$p_uid=$_POST['p_uid'];
}
if (isset($_POST['p_uid_weight'])) {
  $p_uid_weight=$_POST['p_uid_weight'];
}
//============================================================================================================

if (isset($_POST['p_gid'])) {
	$p_gid=$_POST['p_gid'];
}
if (isset($_POST['p_gid_weight'])) {
  $p_gid_weight=$_POST['p_gid_weight'];
}
//============================================================================================================

if (isset($_POST['p_args'])) {
	$p_args=$_POST['p_args'];
}
if (isset($_POST['p_args_weight'])) {
  $p_args_weight=$_POST['p_args_weight'];
}
//============================================================================================================

if (isset($_POST['p_tcp_banner'])) {
  $p_tcp_banner=$_POST['p_tcp_banner'];
}
if (isset($_POST['p_tcp_banner_weight'])) {
  $p_tcp_banner_weight=$_POST['p_tcp_banner_weight'];
}
//============================================================================================================

if (isset($_POST['p_udp_banner'])) {
  $p_udp_banner=$_POST['p_udp_banner'];
}
if (isset($_POST['p_udp_banner_weight'])) {
  $p_udp_banner_weight=$_POST['p_udp_banner_weight'];
}
//============================================================================================================
if (isset($_POST['p_package'])) {
  $p_package=$_POST['p_package'];
}
if (isset($_POST['p_package_weight'])) {
  $p_package_weight=$_POST['p_package_weight'];
}
//============================================================================================================

if (isset($_POST['p_package_type_id'])) {
  if ($_POST['p_package_type_id'] == "dpkg") {
    $p_package_type_id=1;
  }
  if ($_POST['p_package_type_id'] == "rpm") {
    $p_package_type_id=2;
  }
}
if (isset($_POST['p_package_type_id_weight'])) {
  $p_package_type_id_weight=$_POST['p_package_type_id_weight'];
}
//============================================================================================================

if (isset($_POST['p_file'])) {
  $p_file=$_POST['p_file'];
}
if (isset($_POST['p_file_weight'])) {
  $p_file_weight=$_POST['p_file_weight'];
}
//============================================================================================================

if (isset($_POST['pf_dac'])) {
  $pf_dac=$_POST['pf_dac'];
}
if (isset($_POST['pf_dac_weight'])) {
  $pf_dac_weight=$_POST['pf_dac_weight'];
}
//============================================================================================================
if (isset($_POST['pf_uid'])) {
  $pf_uid=$_POST['pf_uid'];
}
if (isset($_POST['pf_uid_weight'])) {
  $pf_uid_weight=$_POST['pf_uid_weight'];
}
//============================================================================================================
if (isset($_POST['pf_gid'])) {
  $pf_gid=$_POST['pf_gid'];
}
if (isset($_POST['pf_gid_weight'])) {
  $pf_gid_weight=$_POST['pf_gid_weight'];
}
//============================================================================================================
if (isset($_POST['p_descr'])) {
  $p_descr=$_POST['p_descr'];
}
//============================================================================================================
if (isset($_POST['p_solution'])) {
  $p_solution=$_POST['p_solution'];
}
//============================================================================================================


// Atualizar tabela use_cases
$stmt=$mysqli->prepare("INSERT INTO use_cases(date,status,
                                                so_id, so_id_weight,
                                                so_version, so_version_weight,
                                                process_name, process_name_weight,
                                                process_uid, process_uid_weight,
                                                process_gid, process_gid_weight,
                                                process_args, process_args_weight,
                                                process_tcp_banner, process_tcp_banner_weight,
                                                process_udp_banner, process_udp_banner_weight,
                                                package_name, package_name_weight,
                                                package_type_id, package_type_id_weight,
                                                process_binary, process_binary_weight,
                                                process_binary_dac, process_binary_dac_weight,
                                                process_binary_uid, process_binary_uid_weight,
                                                process_binary_gid, process_binary_gid_weight)
	                                           VALUES(CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
if ($stmt === FALSE) {
    die ("Mysql Error 1: " . $mysqli->error);
}
$status=1;
$stmt->bind_param('iisssssisisssssssssisssisisis', $status,
                      $so_id, $so_weight,
                      $so_ver, $so_ver_weight,
                      $p_name, $p_name_weight,
                      $p_uid, $p_uid_weight,
                      $p_gid, $p_gid_weight,
                      $p_args, $p_args_weight,
                      $p_tcp_banner, $p_tcp_banner_weight,
                      $p_udp_banner, $p_udp_banner_weight,
                      $p_package, $p_package_weight,
                      $p_package_type_id, $p_package_type_id_weight,
                      $p_file, $p_file_weight,
                      $pf_dac, $pf_dac_weight,
                      $pf_uid, $pf_uid_weight,
                      $pf_gid, $pf_gid_weight);
$stmt->execute();
$stmt->free_result(); 

$stmt=$mysqli->prepare("select id from use_cases ORDER BY id DESC LIMIT 1");
$stmt->execute();
$stmt->bind_result($ultimo_caso);
$stmt->fetch();
$stmt->free_result();


$stmt=$mysqli->prepare("INSERT INTO use_case_desc_solution(case_id,description,solution) VALUES (?,?,?)");
if ($stmt === FALSE) {
    die ("Mysql Error 2: " . $mysqli->error);
}
$stmt->bind_param('iss',$ultimo_caso,$p_descr,$p_solution);
$stmt->execute();
$stmt->free_result(); 
$stmt->close();
header('Location: dashboard.php?register=sucesso');

?>
</body>
</html>























