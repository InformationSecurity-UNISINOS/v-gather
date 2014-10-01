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

echo "novo valor: " . $_POST['novo_valor'] . "<br>";
echo "nova desc: " . $_POST['nova_desc'] . "<br>";
echo "id: " . $_POST['tupla'] . "<br>"; 

?>
</body>
</html>























