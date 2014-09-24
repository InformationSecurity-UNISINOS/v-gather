<?php
include_once 'db.php';
require_once 'xss_clean.php';
 
/*
* Função GeetWeight
* Recupera métricas CBR da base.
*
*/
function GetWeight($mysqli, $descr) {

  if ( $descr == "exato" ) {
    $stmt=$mysqli->prepare("SELECT weight from weight_settings WHERE descr LIKE \'%exato\'%");
    printf("exato: %s\n", $mysqli->error); 
    $stmt->execute();
    $stmt->bind_result($peso_exato);
    $stmt->fetch();
    $stmt->free_result();
    $value=$peso_exato;
  }
  if ( $descr == "alto" ) {
    $stmt=$mysqli->prepare('SELECT weight from weight_settings WHERE descr LIKE \"%alto%\";');
    printf("alto: %s\n", $mysqli->error); 
    $stmt->execute();
    $stmt->bind_result($peso_alto);
    $stmt->fetch();
    $stmt->free_result();
    $value=$peso_alto;
  }
  if ( $descr == "medio" ) {
    $stmt=$mysqli->prepare('SELECT weight from weight_settings WHERE descr LIKE \"%médio%\"');
    printf("medio: %s\n", $mysqli->error); 
    $stmt->execute();
    $stmt->bind_result($peso_medio);
    $stmt->fetch();
    $stmt->free_result();
    $value=$peso_medio;
  }
  if ( $descr == "baixo" ) {
    $stmt=$mysqli->prepare("SELECT weight from weight_settings WHERE descr LIKE '%baixo%'");
    printf("baixo: %s\n", $mysqli->error); 
    $stmt->execute();
    $stmt->bind_result($peso_baixo);
    $stmt->fetch();
    $stmt->free_result();
    $value=$peso_baixo;
  }
  if ( $descr == "desabilitado" ) {
    $stmt=$mysqli->prepare('SELECT weight from weight_settings WHERE descr LIKE \"%desabilitado%\"');
    printf("desabilitado: %s\n", $mysqli->error); 
    $stmt->execute();
    $stmt->bind_result($peso_desabilitado);
    $stmt->fetch();
    $stmt->free_result();
    $value=$peso_desabilitado;
  }
  return $value;
}

 /*
 * Funcão destinada a iniciar a sessao do usuario.
 * Adicionando httponly, secure, domain, path e lifetime no cookie
 *
 */ 
function sec_session_start() {
    $session_name = 'sec_session_id';   // Set a custom session name
    $secure = SECURE;
    // This stops JavaScript being able to access the session id.
    $httponly = true;
    // Forces sessions to only use cookies.
    if (ini_set('session.use_only_cookies', 1) === FALSE) {
        header("Location: ../error.php?err=Could+not+initiate+a+safe+sessio+ini_set)");
        exit();
    }
    // Gets current cookies params.
    $cookieParams = session_get_cookie_params();
    session_set_cookie_params($cookieParams["lifetime"],
        $cookieParams["path"], 
        $cookieParams["domain"], 
        $secure,
        $httponly);
    // Sets the session name to the one set above.
    session_name($session_name);
    session_start();            // Start the PHP session 
    session_regenerate_id();    // regenerated the session, delete the old one. 
}


 /*
 * Funcão destinada a autenticar o usuario
 * utiliza consultas parametrizadas (prepared statements) para consultas ao banco
 * evitando assim, vulnerabilidades do tipo injeção de sql.
 * Também é utilizado sha512 como salt para a senha,
 * este salt é concatenado com o hash da senha do usuário (também em sha512),
 * desta forma, evitamos armazenar senhas em texto plano no banco de dados.
 * Ao utilizar sha512 na transmissao da senha, evitamos que em texto plano ela seja capturada
 * no meio, e a utilização do salt evita que ao ter a base comprometida, as senhas sejam revertidas
 * através de ataques de raimbow tables.
 */ 
function login($email, $password, $mysqli) { 
    // 445fc3655cede6a6c841d08f0776fac92a0118d1d1597046e09909310b2664538642292515aee4737c39826d70508466f5df36417f09274cb470ca4b6857be7a
    if ($stmt = $mysqli->prepare("SELECT id, username, password, salt FROM mgr_users WHERE email = ? LIMIT 1")) {
        $stmt->bind_param('s', $email);     // Bind "$email" to parameter.
        $stmt->execute();                  // Execute the prepared query.
        $stmt->store_result();
 
        // get variables from result.
        $stmt->bind_result($user_id, $username, $db_password, $salt);
        $stmt->fetch();


        // hash the password with the unique salt.
        $password = hash('sha512', $password . $salt);
        if ($stmt->num_rows == 1) {
            // If the user exists we check if the account is locked
            // from too many login attempts 
 
            if (checkbrute($user_id, $mysqli) == true) {
                // Account is locked 
                // Send an email to user saying their account is locked
                return false;
            } else {
                // Check if the password in the database matches
                // the password the user submitted.
                if ($db_password == $password) {
                    // Password is correct!
                    // Get the user-agent string of the user.
                    $ubrowser = $_SERVER['HTTP_USER_AGENT'];
                    $user_browser = xss_clean($ubrowser); // just for sure
                    // XSS protection as we might print this value
                    $uid = preg_replace("/[^0-9]+/", "", $user_id);
                    $_SESSION['user_id'] = $uid;
                    // XSS protection as we might print this value
                    $unclean = preg_replace("/[^a-zA-Z0-9_\-]+/","",$username);
                    $username = xss_clean($unclean); // just for sure
                    $_SESSION['username'] = $username;
                    $_SESSION['login_string'] = hash('sha512',$password . $user_browser);
                    // Login successful.
                    return true;
                } else {
                    // Password is not correct
                    // We record this attempt in the database
                    $now = time();
                    $mysqli->query("INSERT INTO login_attempts(user_id, time) VALUES ('$user_id', '$now')");
                    return false;
                }
            }
        } else {
            // No user exists.
            return false;
        }
    }

}

/*
* Função para verificar quantas tentativas de login (sem sucesso)
* determinado usuário realizou
* Caso tenha realizado mais que 5 tentativas, retorna true
* caso contrário, retorna false
*
*/
function checkbrute($user_id, $mysqli) {
    // Get timestamp of current time 
    $now = time();
    // All login attempts are counted from the past 2 hours. 
    $valid_attempts = $now - (2 * 60 * 60);
 
    if ($stmt = $mysqli->prepare("SELECT time FROM mgr_login_attempts  WHERE user_id = ? AND time > '$valid_attempts'")) {
        $stmt->bind_param('i', $user_id);
 
        // Execute the prepared query. 
        $stmt->execute();
        $stmt->store_result();
 
        if ($stmt->num_rows > 5) {
            return true;
        } else {
            return false;
        }
    }
}

function login_check($mysqli) {
    // Check if all session variables are set 
    if (isset($_SESSION['user_id'],$_SESSION['username'], $_SESSION['login_string'])) {
 
        $user_id = $_SESSION['user_id'];
        $login_string = $_SESSION['login_string'];
        $username = $_SESSION['username'];
 
        // Get the user-agent string of the user.
        $user_browser = $_SERVER['HTTP_USER_AGENT'];
 
        if ($stmt = $mysqli->prepare("SELECT password FROM mgr_users WHERE id = ? LIMIT 1")) {
            // Bind "$user_id" to parameter. 
            $stmt->bind_param('i', $user_id);
            $stmt->execute();   // Execute the prepared query.
            $stmt->store_result();
 
            if ($stmt->num_rows == 1) {
                // If the user exists get variables from result.
                $stmt->bind_result($password);
                $stmt->fetch();
                $login_check = hash('sha512', $password . $user_browser);
 
                if ($login_check == $login_string) {
                    // Logged In!!!! 
                    return true;
                } else {
                    // Not logged in 
                    return false;
                }
            } else {
                // Not logged in 
                return false;
            }
        } else {
            // Not logged in 
            return false;
        }
    } else {
        // Not logged in 
        return false;
    }
}

/*
* Escape da variavel PHP_SELF
*/ 

function esc_url($url) {
 
    if ('' == $url) {
        return $url;
    }
 
    $url = preg_replace('|[^a-z0-9-~+_.?#=!&;,/:%@$\|*\'()\\x80-\\xff]|i', '', $url);
 
    $strip = array('%0d', '%0a', '%0D', '%0A');
    $url = (string) $url;
 
    $count = 1;
    while ($count) {
        $url = str_replace($strip, '', $url, $count);
    }
 
    $url = str_replace(';//', '://', $url);
 
    $url = htmlentities($url);
 
    $url = str_replace('&amp;', '&#038;', $url);
    $url = str_replace("'", '&#039;', $url);
 
    if ($url[0] !== '/') {
        // We're only interested in relative links from $_SERVER['PHP_SELF']
        return '';
    } else {
        return $url;
    }
}
















?>
