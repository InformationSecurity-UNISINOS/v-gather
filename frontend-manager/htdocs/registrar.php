<!DOCTYPE html>
<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start(); 
if(login_check($mysqli) == false) {

        die('You are not authorized to access this page, please login.');
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
						<li><a href="vulnerabilidades.php"><i class="fa fa-warning"></i><span class="hidden-sm text"> Vulnerabilidades</span></a></li>
						<li><a href="agentes.php"><i class="fa fa-eye"></i><span class="hidden-sm text"> Agentes</span></a></li>
						<li><a href="novousuario.php"><i class="fa fa-user"></i><span class="hidden-sm text"> Usuários</span></a></li>
					</ul>
				</div>
				<a href="#" id="main-menu-min" class="full visible-md visible-lg"><i class="fa fa-angle-double-left"></i></a>
			</div>
			<!-- end: Main Menu -->
						
			<!-- start: Content -->
				<div id="content" class="col-lg-10 col-sm-11 ">
					<div class="row"> <!-- INICIO PRIMEIRA LINHA-->
		                <div class="col-lg-12 col-md-12">
		                    <div class="box">
		                        <div class="box-header">
		                            <h2><i class="fa fa-bookmark-o"></i>
		                                <font face="MankSans" size="5pt">Registro de Caso</font>
		                            </h2>
		                        </div>
		                        <div class="box-content">
		                        	<p class="lead">
		                            	Conforme possível, preencha o maior número de campos. As informações serão utilizadas para estruturar um novo caso que fará parte da base de dados de casos. Use este formulário para registrar uma ocorrência de uma vulnerabilidade identificada.
		                           	</p>
		                           	<p>
		                           		A relevância de cada item é um valor no formato ponto flutuante, com duas casas após o ponto.<br>
		                           		Para itens que tem muita relevância para determinar a vulnerabilidade, atribuir valores próximos a 1.<br>
		                           		Por exemplo: <br>
		                           		Se a vulnerabilidade é atribuída a versão específica de um serviço, o valor de relevância pode ser 1 e será atribuído ao campo do pacote do processo.<br>
		                           		Se esta vulnerabilidade pode estar presente tanto no Debian, quanto no CentOS, a relevância deste item pode ser configurada com valores próximos a zero, como 0.2, por exemplo.<br>
		                           		Se a vulnerabilidade pertence a um serviço de rede, atribua mais pontos para os itens banner e portas do serviço<br>

		                           	</p>
		                            <form action="save.php" method="POST" role="form" class="form-horizontal">
		                            	<table class="table table-striped">
		                            		<thead>
		                            			<tr>
		                            				<td>Categoria</td><td>Itens</td><td>Relevância</td>
		                            			</tr>
		                            		</thead>
		                            		<tbody>
												<tr>
													<td>
														Distribuição GNU/Linux
													</td>
													<td>
														<label class="radio-inline">
														    <input type="radio" name="so" id="debian" value="debian" checked> Debian
														 </label>
														<label class="radio-inline">
														   	<input type="radio" name="so" id="centos" value="centos"> CentOS
														 </label>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="so_weight" name="so_weight" type="text" required>
													</td>
												</tr>
												<tr>
													<td>
														Versão da Distribuição GNU/Linux
													</td>
													<td>
														<input placeholder="Exemplo: 7.4" class="form-control focused" id="so_ver" name="so_ver" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="so_ver_weight" name="so_ver_weight" type="text" required>
													</td>
												</tr>
												<tr>
													<td>
														Nome do Processo
													</td>
													<td>
														<input placeholder="Exemplos: apache2, mysqld, ntpd, cron" class="form-control focused" id="p_name" name="p_name" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_name_weight" name="p_name_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														UID do processo
													</td>
													<td>
														<input placeholder="Exemplos: 33, 0, 80"class="form-control focused" id="p_uid" name="p_uid" type="number" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_uid_weight" name="p_uid_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														GID do processo
													</td>
													<td>
														<input placeholder="Exemplos: 33, 0, 80"class="form-control focused" id="p_gid" name="p_gid" type="number" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_gid_weight" name="p_gid_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Argumentos do processo
													</td>
													<td>
														<input placeholder="Exemplos: -k start --config=/etc/config/config.conf"class="form-control focused" id="p_args" name="p_args" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_args_weight" name="p_args_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Banner (TCP)<br>
														<font color="#b8b8b8">
															<i>O banner deve ser capturado através do nmap (-sV)</i>
			                                    		</font>
													</td>
													<td>
														<input placeholder="Exemplos: Apache httpd"class="form-control focused" id="p_tcp_banner" name="p_tcp_banner" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_tcp_banner_weight" name="p_tcp_banner_weight" type="text" required>
													</td>
												</tr>
												<tr>
													<td>
														Portas (TCP) do Serviço
													</td>
													<td>
														<input placeholder="Exemplos: 80,443,8080"class="form-control focused" id="p_tcp_portas" name="p_tcp_portas" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_tcp_portas_weight" name="p_tcp_portas_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Banner (UDP)<br>
														<font color="#b8b8b8">
															<i>O banner deve ser capturado através do nmap (-sUV)</i>
			                                    		</font>
													</td>
													<td>
														<input placeholder="Exemplos: 80,443,8080"class="form-control focused" id="p_udp_banner" name="p_udp_banner" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_udp_banner_weight" name="p_udp_banner_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Portas (UDP) do Serviço
													</td>
													<td>
														<input placeholder="Exemplos: 80,443,8080"class="form-control focused" id="p_udp_portas" name="p_udp_portas" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_udp_portas_weight" name="p_udp_portas_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Arquivo executável do processo
													</td>
													<td>
														<input placeholder="Exemplo: /usr/lib/apache2/mpm-prefork/apache2"class="form-control focused" id="p_file" name="p_file" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_file_weight" name="p_file_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Pacote a qual pertence o processo
													</td>
													<td>
														<input placeholder="Exemplo: apache2-2.2.22"class="form-control focused" id="p_package" name="p_package" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_package_weight" name="p_package_weight" type="text" required>
													</td>
												</tr>
												<tr>
													<td>
														Pacote RPM ou DPKG?
													</td>
													<td>
														<label class="radio-inline">
														    <input type="radio" name="p_package_type_id" id="dpkg" value="dpkg" checked> Dpkg
														 </label>
														<label class="radio-inline">
														   	<input type="radio" name="p_package_type_id" id="rpm" value="rpm"> Rpm
														 </label>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="p_package_type_id_weight" name="p_package_type_id_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Esquema de permissões DAC do arquivo executável do processo
													</td>
													<td>
														<input placeholder="Exemplo: 755, 740"class="form-control focused" id="pf_dac" name="pf_dac" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="pf_dac_weight" name="pf_dac_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														UID do arquivo executável do processo
													</td>
													<td>
														<input placeholder="Exemplo: 0"class="form-control focused" id="pf_uid" name="pf_uid" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="pf_uid_weight" name="pf_uid_weight" type="text" required>
													</td>
												</tr>
												<tr>
													<td>
														GID do arquivo executável do processo
													</td>
													<td>
														<input placeholder="Exemplo: 0"class="form-control focused" id="pf_gid" name="pf_gid" type="text" autocomplete="disabled" required>
													</td>
													<td>
														<input placeholder="0 a 1. Números como 0.6, 0.43 e 0.11, são aceitos" class="form-control focused" id="pf_gid_weight" name="pf_gid_weight" type="text" required>
													</td>
												</tr>

												<tr>
													<td>
														Descrição da vulnerabilidade
													</td>
													<td colspan="2">
														<textarea id="p_descr" name="p_descr" rows="3" style="width:100%" autocomplete="disabled" required></textarea>
													</td>
												</tr>

												<tr>
													<td>
														Solução para vulnerabilidade
													</td>
													<td colspan="2">
														<textarea id="p_solution" name="p_solution" rows="3" style="width:100%" autocomplete="disabled" required></textarea>
													</td>
												</tr>
												<tr>
													<td></td>
													<td></td>
													<td>
														<div class="form-actions">
												  			<button type="submit" class="btn btn-primary">Salvar</button>
														</div>
													</td>
												</tr>


											</tbody>



										</table>

										
									</form>



















		                        </div> <!-- div class box-content -->
		                    </div> <!-- /div class box -->
		                </div> <!-- /div class col-lg-12 col-md-12 -->
					</div> <!--/ FIM PRIMEIRA LINHA-->

				</div> <!-- content -->		
				<div class="col-md-3 visible-md visible-lg" id="feed">
					
					<h2>Activity Feed <a class="fa fa-repeat"></a></h2>
					<ul id="filter">
						<li><a class="green" href="index.html#" data-option-value="task">Tasks</a></li>
						<li><a class="red" href="index.html#" data-option-value="comment">Comments</a></li>
						<li><a class="blue" href="index.html#" data-option-value="message">Messages</a></li>
						<li><a href="index.html#" data-option-value="all">All</a></li>
					</ul>
					
					<ul id="timeline">
						
						<li class="task">
							<i class="fa fa-check-square green"></i>
							<div class="title">New website - A/B Tests</div>
							<div class="desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</div>
							<span class="date">3 seconds ago</span>
							<span class="separator">•</span>
							<span class="name">Megan Abbott</span>
						</li>
						
						<li class="comment">
							<i class="fa fa-comments red"></i>
							<div class="title">Sales increase</div>
							<div class="desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </div>
							<span class="date">15 minutes ago</span>
							<span class="separator">•</span>
							<span class="name">Ashley Tan</span>
						</li>
					</ul>
					<a href="index.html#" id="load-more">•••</a>		
				</div><!--/content-->	
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