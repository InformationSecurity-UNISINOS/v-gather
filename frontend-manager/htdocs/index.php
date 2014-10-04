<!DOCTYPE html>
<html lang="en">
<head>
	
	<!-- start: Meta -->
	<meta charset="utf-8">
	<title>V-GATHER::Manager</title>
	
	<!-- end: Meta -->
	
	<!-- start: Mobile Specific -->
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- end: Mobile Specific -->
	
	<!-- start: CSS -->
	<link href="assets/css/bootstrap.min.css" rel="stylesheet">
	<link href="assets/css/style.min.css" rel="stylesheet">
	<link href="assets/css/retina.min.css" rel="stylesheet">
	<link href="assets/css/print.css" rel="stylesheet" type="text/css" media="print"/>
	<!-- end: CSS -->
	

	<!-- The HTML5 shim, for IE6-8 support of HTML5 elements -->
	<!--[if lt IE 9]>
		
	  	<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
		<script src="assets/js/respond.min.js"></script>
		
	<![endif]-->
	
	<!-- start: Favicon and Touch Icons -->
	<link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
	<link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
	<link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
	<link rel="apple-touch-icon-precomposed" sizes="57x57" href="assets/ico/apple-touch-icon-57-precomposed.png">
	<link rel="shortcut icon" href="assets/ico/favicon.png">
	<!-- end: Favicon and Touch Icons -->	
	 <script type="text/JavaScript" src="assets/js/sha512.js"></script> 
     <script type="text/JavaScript" src="assets/js/forms.js"></script> 

</head>

<body>
		<?php
			include_once 'includes/db_connect.php';
			include_once 'includes/functions.php';

			sec_session_start();
			if (login_check($mysqli) == true) {
    			$logged = 'in';
			} else {
    			$logged = 'out';
			}
		?>

		<div class="container">
		<div class="row">
				<div id="content2" class="col-sm-12 full">
			
			<div class="row">

				<div class="col-lg-4 col-lg-offset-4 col-md-6 col-md-offset-3 login-box-locked type2">
					
					<img src="assets/img/infosec1.png" class="avatar"/>
					
					<h2>V-Gather Manager Panel</h2>
					<p>Por favor, identifique-se:</p>

					<div class="input-prepend input-group">
						<form action="includes/process_login.php" method="post" name="login_form"> 
							<table>
								<tr>
									<td>
										<input id="prependedInput" class="form-control" type="text" placeholder="Email" name="email">
									</td>
								</tr>
								<tr>
									<td>
										<input id="prependedInput" class="form-control" size="16" type="password" placeholder="Password" name="p">
									</td>
									<td>
										<span class="input-group-btn">
											<button class="btn btn-info" type="button" onclick="formhash(this.form, this.form.p);"><i class="fa fa-unlock"></i></button>
			
										</span>
									</td>
								</tr>
							</table>
						</form>
					</div>
					<a href="#">Esqueci a senha</a>
					<?php
        				if (isset($_GET['error'])) {
            				echo 'Usuário ou senha inválida';
        				}
        			?> 

				</div><!--/col-->

			</div><!--/row-->
		
		</div><!--/content-->	

			
			
				</div><!--/row-->		
		
	</div><!--/container-->
	
		
	<!-- start: JavaScript-->
	<!--[if !IE]>-->

			<script src="assets/js/jquery-2.0.3.min.js"></script>

	<!--<![endif]-->

	<!--[if IE]>
	
		<script src="assets/js/jquery-1.10.2.min.js"></script>
	
	<![endif]-->

	<!--[if !IE]>-->

		<script type="text/javascript">
			window.jQuery || document.write("<script src='assets/js/jquery-2.0.3.min.js'>"+"<"+"/script>");
		</script>

	<!--<![endif]-->

	<!--[if IE]>
	
		<script type="text/javascript">
	 	window.jQuery || document.write("<script src='assets/js/jquery-1.10.2.min.js'>"+"<"+"/script>");
		</script>
		
	<![endif]-->
	<script src="assets/js/jquery-migrate-1.2.1.min.js"></script>
	<script src="assets/js/bootstrap.min.js"></script>
	
		
	
	
	<!-- page scripts -->
	<script src="assets/js/jquery.backstretch.min.js"></script>
	
	<!-- theme scripts -->
	<script src="assets/js/custom.min.js"></script>
	<script src="assets/js/core.min.js"></script>
	
	<!-- inline scripts related to this page -->
	<script src="assets/js/pages/page-lockscreen2.js"></script>
	
	<!-- end: JavaScript-->
	
</body>
</html>
