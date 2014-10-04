<!DOCTYPE html>
<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start(); 
if(login_check($mysqli) == false) {

        header('Location: index.php');
}
?>
<html lang="en">
<head>
	
	<!-- start: Meta -->
	<meta charset="utf-8">
	<title>V-Gather::Manager</title>

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
	<!-- start: Header -->
	<header class="navbar">
		<div class="container">
			<button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".sidebar-nav.nav-collapse">
			      <span class="icon-bar"></span>
			      <span class="icon-bar"></span>
			      <span class="icon-bar"></span>
			</button>
			<a id="main-menu-toggle" class="hidden-xs open"><i class="fa fa-bars"></i></a>		
			<a class="navbar-brand col-md-2 col-sm-1 col-xs-2" href="dashboard.php"><span>V-Gather</span></a>
			
		</div>
	</header>
	<div class="container">
		<div class="row">
			<!-- start: Main Menu -->
			<div id="sidebar-left" class="col-lg-2 col-sm-1 ">
								
				<div class="sidebar-nav nav-collapse collapse navbar-collapse">
					<ul class="nav main-menu">
						<li><a href="dashboard.php"><i class="fa fa-dashboard"></i><span class="hidden-sm text"> Dashboard</span></a></li>	
						<li><a href="registrar.php"><i class="fa fa-edit"></i><span class="hidden-sm text"> Registrar Casos</span></a></li>
						<li><a href="visualizar.php"><i class="fa fa-tags"></i><span class="hidden-sm text"> Visualizar Casos</span></a></li>
						<li><a href="Matching.php"><i class="fa fa-warning"></i><span class="hidden-sm text"> Matching</span></a></li>
						<li><a href="endpoints.php"><i class="fa fa-eye"></i><span class="hidden-sm text"> Endpoints</span></a></li>
						<li><a href="novousuario.php"><i class="fa fa-user"></i><span class="hidden-sm text"> Usuários</span></a></li>
						<li><a href="settings.php"><i class="fa fa-wrench"></i><span class="hidden-sm text"> Configurações</span></a></li>
					</ul>
				</div>
				<a href="#" id="main-menu-min" class="full visible-md visible-lg"><i class="fa fa-angle-double-left"></i></a>
			</div>
			<!-- end: Main Menu -->
						
			<!-- start: Content -->
				<div id="content" class="col-lg-10 col-sm-11 ">
					<div class="row">
						<div class="col-sm-12 col-md-9">
							<ol class="breadcrumb">
							  	<li><a href="#">V-Gather</a></li>
							  	<li class="active" >Novo Usuário</li>
							</ol>
							<div class="row">
								<div class="col-lg-12">
									<div class="box">
										<div class="box-header">
											<h2><i class="fa fa-edit"></i>Dados do Novo Usuário</h2>
										</div>
										<div class="box-content">
		                            	
		                           		<span width="30px" height="30px">
		                           			<form action="includes/user_save.php" method="POST" role="form" class="form-horizontal">
										  		<fieldset class="col-sm-12">
			                                  		<div class="form-group">
														<label class="control-label" for="focusedInput">Nome:</label>
															<div class="controls">
												  				<input class="form-control focused" id="username" name="username" type="text" autocomplete="disable" >
															</div>
			                                		</div>
			                                		<div class="form-group">
														<label class="control-label" for="focusedInput">E-Mail:</label>
															<div class="controls">
												  				<input class="form-control focused" id="email" name="email" type="text" autocomplete="disable" >
															</div>
			                                		</div>
			                                		<div class="form-group">
														<label class="control-label" for="focusedInput">Senha:</label>
															<div class="controls">
												  				<input class="form-control focused" id="password" name="password" type="password" autocomplete="disable" >
															</div>
														<label class="control-label" for="focusedInput">Confirmação de Senha:</label>
															<div class="controls">
												  				<input class="form-control focused" id="cpassword" name="cpassword" type="cpassword" autocomplete="disable" >
															</div>
			                                		</div>
			                                		<div class="form-actions">
											  			<button type="submit" class="btn btn-primary" onclick="return regformhash(this.form,
											  																			this.form.username,
											  																			this.form.email,
											  																			this.form.password,
											  																			this.form.cpassword);">Salvar</button>
											  			<button type="reset" class="btn">Cancel</button>
													</div>
				                                </fieldset>
											</form>   
										</span>
									</div>
								</div> <!-- /div col-lg-12-->
							</div><!--/row-->
						</div><!--/col-sm-12 col-md-9-->
					</div> <!-- row -->
				</div> <!-- content -->		
<div class="col-md-3 visible-md visible-lg" id="feed">
					<h2>Activity Feed <a class="fa fa-repeat"></a></h2>
					<ul id="filter">
						<li><a class="green" href="index.html#" data-option-value="task">Casos</a></li>
						<li><a class="red" href="index.html#" data-option-value="comment">Vulnerabilidades</a></li>
						<li><a class="blue" href="index.html#" data-option-value="message">Gerência</a></li>
						<li><a href="index.html#" data-option-value="all">Todos</a></li>
					</ul>
					<ul id="timeline">
						<?php
							include_once 'includes/db_connect.php';
							include_once 'includes/functions.php';
							$stmt=$mysqli->prepare("select id,process_name,package_name,date from use_cases ORDER BY id DESC LIMIT 1");
							if ($stmt === FALSE) {
            					printf('errno: %d, <br>error: %s <br>', $stmt->errno, $stmt->error);
            					die ("Mysql Error: " . $mysqli->error);
        					}
							$stmt->execute();
							$stmt->bind_result($last_case,$last_pname,$last_package,$data);
							$stmt->fetch();
							$stmt->free_result();
							if (!is_null($last_case) && !is_null($last_pname)) {
								echo '<li class="task">';
									echo '<i class="fa fa-check-square green"></i>';
									echo '<div class="title"> Último caso:  '. $last_case .'</div>';
									echo '<div class="desc">Novo caso para o processo ' . $last_pname;
									if (is_null($last_package)) {
										echo '</div>';
									} else {
										echo ' instalado através do pacote versionado '. $last_package .'</div>';
									}
									echo '<span class="date">Em</span>';
									echo '<span class="separator">•</span>';
									echo '<span class="name">'.$data.'</span>';
								echo '</li>';
							}

							$stmt=$mysqli->prepare("select id,ipaddress,hostname,created from managed_servers order by id desc LIMIT 1");
							if ($stmt === FALSE) {
            					printf('errno: %d, <br>error: %s <br>', $stmt->errno, $stmt->error);
            					die ("Mysql Error: " . $mysqli->error);
        					}
							$stmt->execute();
							$stmt->bind_result($last_a_id,$last_a_ip,$last_a_hostname,$last_a_created);
							$stmt->fetch();
							$stmt->free_result();
							if (!is_null($last_a_id) && !is_null($last_a_ip))  {
								echo '<li class="message">';
									echo '<i class="fa fa-eye blue"></i>';
									echo '<div class="title"> Agente Adicionado</div>';
									echo '<div class="desc">Novo agente registrado para o servidor de endereço IP ' . $last_a_ip;
									if (is_null($last_a_hostname)) {
										echo '</div>';
									} else {
										echo ' e hostname '. $last_a_hostname .'</div>';
									}
									echo '<span class="date">Em</span>';
									echo '<span class="separator">•</span>';
									echo '<span class="name">'.$last_a_created.'</span>';
								echo '</li>';
							}

						?>
					</ul>
					<a href="index.html#" id="load-more">•••</a>		
				</div><!--/col-->	
		</div><!--/row-->	
	</div>
			<!-- end: Content -->
				
		</div><!--/row-->		
		
	</div><!--/container-->
	<div class="clearfix"></div>
	
	<footer>
		<p>
			<span style="text-align:left;float:left">V-GATHER</span>
			<span class="hidden-phone" style="text-align:right;float:right">/ DOUGLAS S. SANTOS, JEFERSON C. NOBRE / UNISINOS</span>
		</p>

	</footer>
		
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
	<script src="assets/js/jquery-ui-1.10.3.custom.min.js"></script>
	<script src="assets/js/jquery.ui.touch-punch.min.js"></script>
	<script src="assets/js/jquery.sparkline.min.js"></script>
	<script src="assets/js/fullcalendar.min.js"></script>
	<!--[if lte IE 8]><script language="javascript" type="text/javascript" src="assets/js/excanvas.min.js"></script><![endif]-->
	<script src="assets/js/jquery.flot.min.js"></script>
	<script src="assets/js/jquery.flot.pie.min.js"></script>
	<script src="assets/js/jquery.flot.stack.min.js"></script>
	<script src="assets/js/jquery.flot.resize.min.js"></script>
	<script src="assets/js/jquery.flot.time.min.js"></script>
	<script src="assets/js/jquery.autosize.min.js"></script>
	<script src="assets/js/jquery.placeholder.min.js"></script>
	<script src="assets/js/moment.min.js"></script>
	<script src="assets/js/daterangepicker.min.js"></script>
	<script src="assets/js/jquery.easy-pie-chart.min.js"></script>
	<script src="assets/js/jquery.dataTables.min.js"></script>
	<script src="assets/js/dataTables.bootstrap.min.js"></script>
	
	<!-- theme scripts -->
	<script src="assets/js/custom.min.js"></script>
	<script src="assets/js/core.min.js"></script>
	
	<!-- inline scripts related to this page -->
	<script src="assets/js/pages/index.js"></script>
	
	<!-- end: JavaScript-->
	
</body>
</html>