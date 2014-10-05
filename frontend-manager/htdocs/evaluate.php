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
						<li><a href="visualizar.php"><i class="fa fa-tags"></i><span class="hidden-sm text"> Ver Casos</span></a></li>
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
					  	<li class="active" >Possíveis Casos Encontrados</li>
					</ol>
					
					<div class="row">

							<div class="col-lg-12 col-md-12"> <!-- Casos -->
                                <div class="box">
                                    <div class="box-header">
                                        <h2><i class="fa fa-bookmark-o"></i>
                                            <font face="MankSans" size="5pt">Matching</font>
                                        </h2>
                                    </div>
                                    
                                    <font face="MankSans" size="2pt">
                                        <div class="box-content">
											<?php
                                        		include_once 'includes/db_connect.php';
												include_once 'includes/functions.php';

												$stmt = $mysqli->prepare("SELECT id FROM use_cases WHERE status = 2 ORDER BY candidate_final_score DESC");
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
											        // ===============================================
											        // recupera o candidato 
											        // ===============================================
											        $stmt2 = $mysqli->prepare("SELECT id,date, case_id_related,
			                                               so_id, so_id_score, 
			                                               so_version, so_version_score,
			                                               process_name, process_name_score,
			                                               process_uid, process_uid_score,
			                                               process_gid, process_gid_score,
			                                               process_args, process_args_score,
			                                               process_tcp_banner, process_tcp_banner_score,
			                                               process_udp_banner, process_udp_banner_score,
			                                               package_name, package_name_score,
			                                               process_binary, process_binary_score, candidate_final_score
			                                              FROM use_cases WHERE id = ?");
											        if ($stmt2 === FALSE) {
	            										die ("Mysql Error: " . $mysqli->error);
        											}
													$stmt2->bind_param('i', $field);
														
												    $stmt2->execute();
													$stmt2->bind_result($case_id,$date,$case_related,
												        					$so_id, $so_id_score,
												        					$so_version, $so_version_score,
																			$process_name, $process_name_score,
																			$process_uid, $process_uid_score,
																			$process_gid, $process_gid_score,
																			$process_args, $process_args_score,
																			$process_tcp_banner, $process_tcp_banner_score,
																			$process_udp_banner, $process_udp_banner_score,
																			$package_name, $package_name_score,
																			$process_binary, $process_binary_score,
																			$candidate_final_score);
													$stmt2->fetch();
													$stmt2->free_result(); 

													// ===============================================
											        // recupera o caso relacionado para comparar 
											        // ===============================================
													$stmt2 = $mysqli->prepare("SELECT id,date,
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
			                                               	FROM use_cases WHERE id = ?");
													$stmt2->bind_param('i', $case_related);
														
												    $stmt2->execute();
													$stmt2->bind_result($r_case_id,$r_date,
												        					$r_so_id, $r_so_id_weight,
												        					$r_so_version, $r_so_version_weight,
																			$r_process_name, $r_process_name_weight,
																			$r_process_uid, $r_process_uid_weight,
																			$r_process_gid, $r_process_gid_weight,
																			$r_process_args, $r_process_args_weight,
																			$r_process_tcp_banner,$r_process_tcp_banner_weight,
																			$r_process_udp_banner,$r_process_udp_banner_weight,
																			$r_package_name, $r_package_name_weight,
																			$r_process_binary, $r_process_binary_weight);
													$stmt2->fetch();
													$stmt2->free_result(); 

													echo '<table class="table table-bordered table-striped table-condensed" style="text-align:center;">';
	                                                	echo '<thead>';
	                                                		echo '<tr>';
	                                                			echo '<th style="text-align:center;background:#34383c;" colspan="5"><font color="#FFFFFF">MATCH: ' . $i . " SCORE: " . round($candidate_final_score,4) .'</font></th>';
	                                                		echo '</tr>';
	                                                		echo '<tr>';
	                                                			echo '<th style="text-align:center;background:#929497;" > - </th>';
	                                                				echo '<th style="text-align:center;background:#929497;" colspan="2"><font color="#FFFFFF">CANDIDATO</font></th>';
	                                                				echo '<th style="text-align:center;background:#929497;" colspan="2"><font color="#FFFFFF">CASO RELACIONADO</font></th>';
	                                                		echo '</tr>';
	                                                    	echo '<tr>';
	                                                        	echo '<th style="text-align:center;" width="20%">Itens</th>';
	                                                        	echo '<th style="text-align:center;" width="30%">Dados</th>';
	                                                        	echo '<th style="text-align:center;" width="20%">Score</th>';
	                                                        	echo '<th style="text-align:center;" width="10%">Dados</th>';
	                                                        	echo '<th style="text-align:center;" width="10%">Peso</th>';
	                                                    	echo '</tr>';
	                                                	echo '</thead>';
	                                                	echo '<tbody>';

														$stmt2= $mysqli->prepare("SELECT name FROM sos WHERE id = ?");
														$stmt2->bind_param('i', $so_id);
														$stmt2->execute();
														$stmt2->bind_result($soname);
														$stmt2->fetch();
														$stmt2->free_result();

														$stmt2= $mysqli->prepare("SELECT name FROM sos WHERE id = ?");
														$stmt2->bind_param('i', $r_so_id);
														$stmt2->execute();
														$stmt2->bind_result($r_soname);
														$stmt2->fetch();
														$stmt2->free_result();
	                                                			 
	                                                    echo '<tr align="center">';
	                                                        echo '<td>'. "SO" .'</td>';
	                                                        echo '<td width="30%">'. $soname .'</td>';
	                                                        echo '<td width="10%"> '. round($so_id_score,3) .'</td>';
	                                                        echo '<td width="30%">'. $r_soname .'</td>';
	                                                        echo '<td width="10%"> '. round($r_so_id_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	echo '<tr align="center">';
	                                                        echo '<td>'. "Versão SO" .'</td>';
	                                                        echo '<td width="30%">'. $so_version .'</td>';
	                                                       	echo '<td width="10%">'. round($so_version_score,3) .'</td>';
	                                                       	echo '<td width="30%">'. $r_so_version .'</td>';
	                                                       	echo '<td width="10%">'. round($r_so_version_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	echo '<tr align="center">';
	                                                       	echo '<td>'. "Processo" .'</td>';
	                                                        echo '<td width="30%">'. $process_name .'</td>';
	                                                        echo '<td width="10%">'. round($process_name_score,3) .'</td>';
	                                                        echo '<td width="30%">'. $r_process_name .'</td>';
	                                                        echo '<td width="10%">'. round($r_process_name_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	echo '<tr align="center">';
	                                                        echo '<td >'. "UID do Processo" .'</td>';
	                                                        echo '<td width="30%">'. $process_uid .'</td>';
	                                                        echo '<td width="10%">'. round($process_uid_score,3) .'</td>';
	                                                        echo '<td width="30%">'. $r_process_uid .'</td>';
	                                                        echo '<td width="10%">'. round($r_process_uid_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	echo '<tr align="center">';
	                                                        echo '<td >'. "GID do Processo" .'</td>';
	                                                        echo '<td width="30%">'. $process_gid .'</td>';
	                                                        echo '<td width="10%">'. round($process_gid_score,3) .'</td>';
	                                                        echo '<td width="30%">'. $r_process_gid .'</td>';
	                                                        echo '<td width="10%">'. round($r_process_gid_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	echo '<tr align="center">';
	                                                        echo '<td >'. "Argumentos do Processo" .'</td>';
	                                                        echo '<td width="30%">'. $process_args .'</td>';
	                                                        echo '<td width="10%">'. round($process_args_score,3) .'</td>';
	                                                        echo '<td width="30%">'. $r_process_args .'</td>';
	                                                        echo '<td width="10%">'. round($r_process_args_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	echo '<tr align="center">';
	                                                        echo '<td >'. "Pacote do Processo" .'</td>';
	                                                        echo '<td width="30%">'. $package_name .'</td>';
	                                                        echo '<td width="10%">'. round($package_name_score,3) .'</td>';
	                                                        echo '<td width="30%">'. $r_package_name .'</td>';
	                                                        echo '<td width="10%">'. round($r_package_name_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	echo '<tr align="center">';
	                                                        echo '<td >'. "Binário do Processo" .'</td>';
	                                                       	echo '<td width="30%">'. $process_binary .'</td>';
	                                                        echo '<td width="10%">'. round($process_binary_score,3) .'</td>';
	                                                        echo '<td width="30%">'. $r_process_binary .'</td>';
	                                                       	echo '<td width="10%">'. round($r_process_binary_weight,3) .'</td>';
	                                                   	echo '</tr>';

	                                                   	 echo '<tr align="center">';
	                                                        echo '<td >'. "Banner de serviço TCP:" .'</td>';
	                                                        echo '<td width="30%">'. $process_tcp_banner .'</td>';
	                                                        echo '<td width="10%">'. round($process_tcp_banner_score,3) .'</td>';
	                                                       	echo '<td width="30%">'. $r_process_tcp_banner .'</td>';
	                                                        echo '<td width="10%">'. round($r_process_tcp_banner_weight,3) .'</td>';
	                                                   	 echo '</tr>';

														echo '<tr align="center">';
	                                                       	echo '<td >'. "Banner de serviço UDP:" .'</td>';
	                                                       	echo '<td width="30%">'. $process_udp_banner .'</td>';
	                                                       	echo '<td width="10%">'. round($process_udp_banner_score,2) .'</td>';
	                                                       	echo '<td width="30%">'. $r_process_udp_banner .'</td>';
	                                                        echo '<td width="10%"> '. round($r_process_udp_banner_weight,3) .'</td>';
	                                                   	 echo '</tr>';
	                                                   	 		
														$stmt2=$mysqli->prepare("SELECT solution,description FROM use_case_desc_solution WHERE case_id = ?");
														$stmt2->bind_param('i', $case_related);
														$stmt2->execute();
														$stmt2->bind_result($solucao,$descricao);
														$stmt2->fetch();
														$stmt2->free_result();

	                                                   	echo '<tr align="center">';
	                                                       	echo '<td>'. "Descrição do Caso Relacionado" .'</td>';
	                                                        echo '<td colspan="4">'. $descricao .'</td>';
	                                                   	 echo '</tr>';

	                                                   	 echo '<tr align="center">';
	                                                       	echo '<td>'. "Solução do Caso Relacionado" .'</td>';
	                                                       	echo '<td colspan="4">'. $solucao .'</td>';
	                                                   	 echo '</tr>';

	                                                   	 echo '<tr>';
	                                                   	 	echo '<td>Deseja eleger este como melhor caso e aplicar a solução?</td>'; 
															echo '<td colspan="4">';

																// The above code should be checked against CSRF vulnerability:
																// This webconsole should not be published on production server.
																// THIS IS A POC OF AN ARTICLE, NOT A PROFESSIONAL TOOL. DO NOT USE ON YOUR ENVIRONMENT
																// DUE TO SECURITY ISSUES.
																echo '<form action="reject.php?field='.$field.'" method="POST" role="form" class="form-horizontal">';
																	echo '<button type="submit" class="btn btn-default"><i class="fa fa-trash-o"> Rejeitar </i></button>';
																echo '</form>';
																echo '<form action="apply.php?field='.$field.'" method="POST" role="form" class="form-horizontal">';
																	echo '<button type="submit" class="btn btn-primary" ><i class="fa fa-mail-forward"> Aplicar </i></button>';
																echo '</form>';
															echo '</td>';
														echo '</tr>';

	                                               	echo '</tbody>';
	                                            echo '</table>';
											    } 
											    $stmt->close();
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