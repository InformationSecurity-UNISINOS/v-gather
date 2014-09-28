<html>
<body>
<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';
include_once 'includes/xss_clean.php';


sec_session_start(); 
if(login_check($mysqli) == false) {

        header('Location: index.php');
        die();
}

if (isset($_POST['so'])) {
	if ($_POST['so'] == "debian") {
    $so_id=1;
  }
  if ($_POST['so'] == "centos") {
    $so_id=2;
  }
}

if (isset($_POST['so_peso'])) {
  $so_weight=GetWeight($mysqli,$_POST['so_peso']);
}
//============================================================================================================

if (isset($_POST['so_ver'])) {
    $so_ver=xss_clean($_POST['so_ver']);
}
if (isset($_POST['so_ver_peso'])) {
  $so_ver_weight=GetWeight($mysqli,$_POST['so_ver_peso']);

}
//============================================================================================================

if (isset($_POST['p_name'])) {
	$p_name=xss_clean($_POST['p_name']);
}
if (isset($_POST['p_name_peso'])) {
  $p_name_weight=GetWeight($mysqli,$_POST['p_name_peso']);
 
}
//============================================================================================================

if (isset($_POST['p_uid'])) {
	$p_uid=xss_clean($_POST['p_uid']);
}
if (isset($_POST['p_uid_peso'])) {

  $p_uid_weight=GetWeight($mysqli,$_POST['p_uid_peso']);
}
//============================================================================================================

if (isset($_POST['p_gid'])) {
	$p_gid=xss_clean($_POST['p_gid']);
}
if (isset($_POST['p_gid_peso'])) {
  $p_gid_weight=GetWeight($mysqli,$_POST['p_gid_peso']);
}
//============================================================================================================

if (isset($_POST['p_args'])) {
	$p_args=xss_clean($_POST['p_args']);
}
if (isset($_POST['p_args_peso'])) {
  $p_args_weight=GetWeight($mysqli,$_POST['p_args_peso']);
}
//============================================================================================================

if (isset($_POST['p_tcp_banner'])) {
  $p_tcp_banner=xss_clean($_POST['p_tcp_banner']);
}
if (isset($_POST['p_tcp_banner_peso'])) {
  $p_tcp_banner_weight=GetWeight($mysqli,$_POST['p_tcp_banner_peso']);
}
//============================================================================================================

if (isset($_POST['p_udp_banner'])) {
  $p_udp_banner=xss_clean($_POST['p_udp_banner']);
}
if (isset($_POST['p_udp_banner_peso'])) {
  $p_udp_banner_weight=GetWeight($mysqli,$_POST['p_udp_banner_peso']);
}
//============================================================================================================
if (isset($_POST['p_package'])) {
  $p_package=xss_clean($_POST['p_package']);
}
if (isset($_POST['p_package_peso'])) {
  $p_package_weight=GetWeight($mysqli,$_POST['p_package_peso']);
}

//============================================================================================================

if (isset($_POST['p_file'])) {
  $p_file=xss_clean($_POST['p_file']);
}
if (isset($_POST['p_file_peso'])) {
  $p_file_weight=GetWeight($mysqli,$_POST['p_file_peso']);
}
//============================================================================================================
if (isset($_POST['p_descr'])) {
  $p_descr=xss_clean($_POST['p_descr']);
}
//============================================================================================================
if (isset($_POST['p_solution'])) {
  $p_solution=xss_clean($_POST['p_solution']);
}
//============================================================================================================
// Atualizar tabela use_cases
$stmt=$mysqli->prepare("INSERT INTO use_cases(date,status,origem,
                                                so_id, so_id_weight,
                                                so_version, so_version_weight,
                                                process_name, process_name_weight,
                                                process_uid, process_uid_weight,
                                                process_gid, process_gid_weight,
                                                process_args, process_args_weight,
                                                process_tcp_banner, process_tcp_banner_weight,
                                                process_udp_banner, process_udp_banner_weight,
                                                package_name, package_name_weight,
                                                process_binary, process_binary_weight)
	                                           VALUES(CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
if ($stmt === FALSE) {
    die ("Mysql Error 1: " . $mysqli->error);
}
$status=1;
$origem=1;
$stmt->bind_param('ssssssssssssssssssssssss', $status, $origem,
                      $so_id, $so_weight,
                      $so_ver, $so_ver_weight,
                      $p_name, $p_name_weight,
                      $p_uid, $p_uid_weight,
                      $p_gid, $p_gid_weight,
                      $p_args, $p_args_weight,
                      $p_tcp_banner, $p_tcp_banner_weight,
                      $p_udp_banner, $p_udp_banner_weight,
                      $p_package, $p_package_weight,
                      $p_file, $p_file_weight);
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























