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
		<div class="container">
		<div class="row">
				
			<!-- start: Main Menu -->
			<div id="sidebar-left" class="col-lg-2 col-sm-1 ">
								
				<div class="sidebar-nav nav-collapse collapse navbar-collapse">
					<ul class="nav main-menu">
						<li><a href="dashboard.php"><i class="fa fa-dashboard"></i><span class="hidden-sm text"> Dashboard</span></a></li>	
						<li><a href="registrar.php"><i class="fa fa-edit"></i><span class="hidden-sm text"> Registrar Casos</span></a></li>
						<li><a href="visualizar.php"><i class="fa fa-tags"></i><span class="hidden-sm text"> Visualizar Casos</span></a></li>
						<li><a href="matching.php"><i class="fa fa-dot-circle-o"></i><span class="hidden-sm text"> Matching</span></a></li>
						<li><a href="evaluate.php"><i class="fa fa-gears"></i><span class="hidden-sm text"> Avaliação</span></a></li>
						<li><a href="endpoints.php"><i class="fa fa-eye"></i><span class="hidden-sm text"> Endpoints</span></a></li>
						<li><a href="novousuario.php"><i class="fa fa-users"></i><span class="hidden-sm text"> Usuários</span></a></li>
						<li><a href="settings.php"><i class="fa fa-wrench"></i><span class="hidden-sm text"> Configurações</span></a></li>
					</ul>
				</div>
				<a href="#" id="main-menu-min" class="full visible-md visible-lg"><i class="fa fa-angle-double-left"></i></a>
			</div>
			<!-- end: Main Menu -->
						
			<!-- start: Content -->
			<div id="content" class="col-lg-10 col-sm-11 ">
			
			
			  <div class="row">
				
				<div class="col-sm-12 col-md-12">
					<ol class="breadcrumb">
					  	<li><a href="#">V-Gather</a></li>
					  	<li class="active" >Visualizar Casos</li>
					</ol>
					
					<div class="row">

							<div class="col-lg-12 col-md-12"> <!-- Casos -->
                                <div class="box">
                                    <div class="box-header">
                                        <h2><i class="fa fa-bookmark-o"></i>
                                            <font face="MankSans" size="5pt">Casos</font>
                                        </h2>
                                    </div>
                                    
                                    <font face="MankSans" size="2pt">
                                        <div class="box-content">
                                        	<?php
                                        		include_once 'includes/db_connect.php';
												include_once 'includes/functions.php';

												$stmt = $mysqli->prepare("SELECT id FROM use_cases WHERE status = 3 ORDER BY candidate_final_score DESC");
												$stmt->execute();
												$i=0;
												$row = array();
												$res = array();
												stmt_bind_assoc($stmt, $row);
												while ($stmt->fetch()) {
											    	foreach($row as $key => $field) {
											        	$res[$i]=$field;
											        	$i++;
											        }
											    }
											    $i=0;
											    $stmt->free_result();
											    foreach($res as $key => $field) {
											    	$i++;
														$stmt2 = $mysqli->prepare("SELECT id,date, origem,
			                                                so_id, so_id_weight,
			                                                so_version, so_version_weight,
			                                                process_name, process_name_weight,
			                                                process_uid, process_uid_weight,
			                                                process_gid, process_gid_weight,
			                                                process_args, process_args_weight,
			                                                process_tcp_banner, process_tcp_banner_weight,
			                                                process_udp_banner, process_udp_banner_weight,
			                                                package_name, package_name_weight,
			                                                process_binary, process_binary_weight
			                                               	FROM use_cases WHERE id = ? AND status=1");
														$stmt2->bind_param('i', $field);
														
												        $stmt2->execute();
														$stmt2->bind_result($case_id,$date,$origem,
												        					$so_id, $so_id_weight,
												        					$so_version, $so_version_weight,
																			$process_name, $process_name_weight,
																			$process_uid, $process_uid_weight,
																			$process_gid, $process_gid_weight,
																			$process_args, $process_args_weight,
																			$process_tcp_banner,$process_tcp_banner_weight,
																			$process_udp_banner,$process_udp_banner_weight,
																			$package_name, $package_name_weight,
																			$process_binary, $process_binary_weight);
														$stmt2->fetch();
														$stmt2->free_result(); 

														echo '<table class="table table-bordered table-striped table-condensed" style="text-align:center;">';
	                                                		echo '<thead>';
	                                                			echo '<tr>';
	                                                					echo '<th style="text-align:center;background:#34383c;" colspan="3"><font color="#FFFFFF">CASO ' . htmlentities($case_id) . '</font></th>';	                                                					

	                                                			echo '</tr>';
	                                                			echo '<tr>';
	                                                			if ($origem == 1) { 
	                                                				echo '<th style="text-align:center;">Registrado em</th>';
	                                                        		echo '<th style="text-align:center;">'. htmlentities($date) .'</th>';
	                                                        		echo '<th style="text-align:center;"></th>';
	                                                        	} else {
	                                                        		echo '<th style="text-align:center;">Aprendido em</th>';
	                                                        		echo '<th style="text-align:center;">'. htmlentities($date) .'</th>';
	                                                        		echo '<th style="text-align:center;"></th>';
	                                                        	}
	                                                			echo '</tr>';
	                                                    		echo '<tr>';
	                                                        		echo '<th style="text-align:center;" width="100px">Itens</th>';
	                                                        		echo '<th style="text-align:center;">Valores</th>';
	                                                        		echo '<th style="text-align:center;" width="100px">Peso</th>';
	                                                    		echo '</tr>';
	                                                		echo '</thead>';
	                                                		echo '<tbody>';

	                                                			$stmt2 = $mysqli->prepare("SELECT name FROM sos WHERE id = ?");
																$stmt2->bind_param('i', $so_id);
														        $stmt2->execute();
																$stmt2->bind_result($soname);
																$stmt2->fetch();
																$stmt2->free_result();
	                                                			 
	                                                    		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "SO" .'</td>';
	                                                        		echo '<td>'.  htmlentities($soname) .'</td>';
	                                                        		echo '<td width="20%"> '.  htmlentities(round($so_id_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "Versão SO" .'</td>';
	                                                        		echo '<td>'.  htmlentities($so_version) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($so_version_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "Processo" .'</td>';
	                                                        		echo '<td>'.  htmlentities($process_name) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($process_name_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "UID do Processo" .'</td>';
	                                                        		echo '<td>'.  htmlentities($process_uid) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($process_uid_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "GID do Processo" .'</td>';
	                                                        		echo '<td>'.  htmlentities($process_gid) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($process_gid_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "Argumentos do Processo" .'</td>';
	                                                        		echo '<td>'.  htmlentities($process_args) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($process_args_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "Pacote do Processo" .'</td>';
	                                                        		echo '<td>'.  htmlentities($package_name) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($package_name_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "Binário do Processo" .'</td>';
	                                                        		echo '<td>'.  htmlentities($process_binary) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($process_binary_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "Banner de serviço TCP:" .'</td>';
	                                                        		echo '<td>'.  htmlentities($process_tcp_banner) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($process_tcp_banner_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td width="20%">'. "Banner de serviço UDP:" .'</td>';
	                                                        		echo '<td>'.  htmlentities($process_udp_banner) .'</td>';
	                                                        		echo '<td width="20%">'.  htmlentities(round($process_udp_banner_weight,3)) .'</td>';
	                                                   	 		echo '</tr>';
	                                                   	 		
																$stmt2=$mysqli->prepare("SELECT solution,description FROM use_case_desc_solution WHERE case_id = ?");
																$stmt2->bind_param('i', $case_id);
														        $stmt2->execute();
																$stmt2->bind_result($solucao,$descricao);
																$stmt2->fetch();
																$stmt2->free_result();

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td>Descrição do Caso</td>';
	                                                        		echo '<td colspan="2">'. htmlentities($descricao) .'</td>';
	                                                   	 		echo '</tr>';

	                                                   	 		echo '<tr align="center">';
	                                                        		echo '<td>Solução do Caso</td>';
	                                                        		echo '<td colspan="2">'. htmlentities($solucao) .'</td>';
	                                                   	 		echo '</tr>';
	                                               			echo '</tbody>';
	                                            		echo '</table>';
											    }
	                                            
                                            ?>
                                        </div>
                                    </font>
                                </div>
                            </div> <!-- /Criterios de Impacto -->
					</div><!--/row-->


				</div><!--/col-->
				
			
				
			</div><!--/row-->	
			
			
			
							
			
     
					
			</div>
			<!-- end: Content -->
				
				</div><!--/row-->		
		
	</div><!--/container-->
	
	
	<div class="modal fade" id="myModal">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
					<h4 class="modal-title">Modal title</h4>
				</div>
				<div class="modal-body">
					<p>Here settings can be configured...</p>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
					<button type="button" class="btn btn-primary">Save changes</button>
				</div>
			</div><!-- /.modal-content -->
		</div><!-- /.modal-dialog -->
	</div><!-- /.modal -->
	
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