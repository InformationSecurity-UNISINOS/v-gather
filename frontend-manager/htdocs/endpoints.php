<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start(); 
if(login_check($mysqli) == false) {

        header('Location: index.php');
}

?>
<!DOCTYPE html>
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
	<!-- end: Header -->
		<div class="container">
			<div class="row">
			<!-- start: Main Menu -->
			<div id="sidebar-left" class="col-lg-2 col-sm-1 ">
								
				<div class="sidebar-nav nav-collapse collapse navbar-collapse">
					<ul class="nav main-menu">
						<li><a href="dashboard.php"><i class="fa fa-dashboard"></i><span class="hidden-sm text"> Dashboard</span></a></li>	
						<li><a href="registrar.php"><i class="fa fa-edit"></i><span class="hidden-sm text"> Registrar Casos</span></a></li>
						<li><a href="visualizar.php"><i class="fa fa-tags"></i><span class="hidden-sm text"> Visualizar Casos</span></a></li>
						<li><a href="matching.php"><i class="fa fa-warning"></i><span class="hidden-sm text"> Matching</span></a></li>
						<li><a href="evaluate.php"><i class="fa fa-gearss"></i><span class="hidden-sm text"> Avaliação</span></a></li>
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
						<ol class="breadcrumb">
					  		<li><a href="#">V-Gather</a></li>
					  		<li class="active" >Endpoints</li>
						</ol>

						<div class="col-sm-12 col-md-12">
							<div class="box">
								<div class="box-header" data-original-title>
									<h2><i class="fa fa-eye"></i><span class="break"></span>Adicionar Endpoint</h2>
								</div>
								<div class="box-content">
									<table class="table table-striped">
										<form action="action.php?mode=endpoint" method="POST" role="form" class="form-horizontal">
				                            <tr>
												<td>
													Hostname:
												</td>
												<td>
													<input class="form-control focused" id="new_ag_hostname" name="new_ag_hostname" type="text" autocomplete="disabled" required>
												</td>
												<td>
													Endereço IP:
												</td>
												<td>
													<input class="form-control focused" id="new_ag_ipaddr" name="new_ag_ipaddr" type="text" autocomplete="disabled" required>
												</td>
												<td width="30%">
													<div class="form-actions">
											  			<button type="submit" class="btn btn-primary">Salvar</button>
													</div>
												<td>
											</tr>
										</form>
									</table>
								</div>
							</div> 
						</div> <!-- col -->
					</div> <!-- row -->
					<div class="row">		
						<div class="col-sm-12 col-md-12">
							<div class="box">
								<div class="box-header" data-original-title>
									<h2><i class="fa fa-user"></i><span class="break"></span>Servidores Gerenciados</h2>
								<!--
									<div class="box-icon">
										<a href="table.html#" class="btn-setting"><i class="fa fa-wrench"></i></a>
										<a href="table.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>
										<a href="table.html#" class="btn-close"><i class="fa fa-times"></i></a>
									</div>
								-->
								</div>
								<div class="box-content">
									<table class="table table-striped table-bordered">
							  			<thead>
										  <tr>
											  <th>Hostname</th>
											  <th>Endereço IP</th>
											  <th>Criado em</th>
											  <th>Atualizado em</th>
											  <th>Status</th>
											  <th>Ações</th>
										  </tr>
										</thead>   
										<tbody>
											<?php
												include_once 'includes/db_connect.php';
												include_once 'includes/functions.php';
												$stmt=$mysqli->prepare("SELECT COUNT(id) FROM managed_servers");
												if ($stmt === FALSE) {
            												printf('errno: %d, <br>error: %s <br>', $stmt->errno, $stmt->error);
            												die ("Mysql Error: " . $mysqli->error);
        										}
												$stmt->execute();
												$stmt->bind_result($nro_servers);
												$stmt->fetch();
												$stmt->free_result(); 

												if ($nro_servers) {
													for ($i = 1; $i <= $nro_servers; $i++) {
														$stmt = $mysqli->prepare("SELECT ipaddress,hostname,created,updated FROM managed_servers WHERE id = ?");
														$stmt->bind_param('i', $i);
												        $stmt->execute();
														$stmt->bind_result($ag_ipaddr,$ag_hostname,$ag_ctime,$ag_mtime);
														$stmt->fetch();
														$stmt->free_result(); 

														echo '<tr>';
															echo '<td>'.$ag_hostname.'</td>';
															echo '<td>'.$ag_ipaddr.'</td>';
															echo '<td>'.$ag_ctime.'</td>';
															echo '<td>'.$ag_mtime.'</td>';
															echo '<td>';
																echo '<span class="label label-success">Ativo</span>';
															echo '</td>';
															echo '<td>';
																echo '<a class="btn btn-success" href="#">';
																	echo '<i class="fa fa-search-plus "></i> ';
																echo '</a>';
																echo '<a class="btn btn-info" href="#">';
																	echo '<i class="fa fa-edit "></i>';
																echo '</a>';
																echo '<a class="btn btn-danger" href="#">';
																	echo '<i class="fa fa-trash-o "></i>';
																echo '</a>';
															echo '</td>';
														echo '</tr>';
													}
												} else {
													echo '<tr>';
													echo '<td colspan="6">';
													echo 'Até o momento, não existem endpoints registrados.';
													echo '</td>';
													echo '</tr>';
												}
												$stmt->close();
											?>
											
										</tbody>
							  		</table>            
								</div>
							</div>
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
	<script src="assets/js/jquery.sparkline.min.js"></script>
	<script src="assets/js/jquery.dataTables.min.js"></script>
	<script src="assets/js/dataTables.bootstrap.min.js"></script>
	
	<!-- theme scripts -->
	<script src="assets/js/custom.min.js"></script>
	<script src="assets/js/core.min.js"></script>
	
	<!-- inline scripts related to this page -->
	<script src="assets/js/pages/table.js"></script>
	
	<!-- end: JavaScript-->
	
</body>
</html>