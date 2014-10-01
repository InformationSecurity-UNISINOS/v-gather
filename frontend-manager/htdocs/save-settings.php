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
?>
</body>
</html>























