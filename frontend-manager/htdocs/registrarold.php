<!DOCTYPE html>
<html lang="en">
<head>
	<!-- start: Meta -->
	<meta charset="utf-8">
	<title>V-GATHER > Registro de caso</title>
	<!-- end: Meta -->
	<!-- start: CSS -->
	<link href="assets/css/bootstrap.min.css" rel="stylesheet">
	<link href="assets/css/style.min.css" rel="stylesheet">
	<link href="assets/css/retina.min.css" rel="stylesheet">
	<link href="assets/css/print.css" rel="stylesheet" type="text/css" media="print"/>
	<!-- end: CSS -->
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
			<a class="navbar-brand col-md-2 col-sm-1 col-xs-2" href="index.html"><span>V-Gather</span></a>
			
			<!-- start: Header Menu -->
			<div class="nav-no-collapse header-nav">
				<ul class="nav navbar-nav pull-right">
        
					<!-- start: User Dropdown -->
					<li class="dropdown">
						<a class="btn account dropdown-toggle" data-toggle="dropdown" href="#">
							<i class="fa fa-tasks"></i>
							<div class="user">
								<span class="name">Menu</span>
                                <span class="name"></span>
							</div>
						</a>
						<ul class="dropdown-menu">
							<li><a href="page-pricing-tables.html#"><i class="fa  fa-pencil"></i> Registrar Caso</a></li>
							<li><a href="page-pricing-tables.html#"><i class="fa fa-bars"></i> Listar Casos</a></li>
							<li><a href="page-pricing-tables.html#"><i class="fa fa-user"></i> Gerenciar Agentes</a></li>
							<li><a href="page-login.html"><i class="fa fa-check-square-o"></i> Casos Encontrados</a></li>
                            <li><a href="page-login.html"><i class="fa fa-exclamation-circle"></i> Vulnerabilidades</a></li>
						</ul>
					</li>
					<!-- end: User Dropdown -->
					
				</ul>
			</div>
			<!-- end: Header Menu -->
			
		</div>	
	</header>
	<!-- end: Header -->
	
		<div class="container">
		<div class="row">

			<!-- start: Content -->
			<div id="content" class="col-lg-10 col-sm-11 ">
							
			<div class="row">
				<div class="col-lg-12">
					<div class="box">
						<div class="box-header">
							<h2><i class="fa fa-edit"></i>REGISTRO DE CASO</h2>
						</div>
						<div class="box-content">
                            <span>
                            Conforme possível, preencha o maior número de campos. As informações serão utilizadas para estruturar um novo caso que fará parte da base de dados de casos. Use este formulário para registrar uma ocorrência de uma vulnerabilidade identificada.
                           </span><span width="30px" height="30px">
                           <form action="save.php" method="POST" role="form" class="form-horizontal">
							  <fieldset class="col-sm-12">
                                  <div class="form-group">
									<label class="control-label">O sistema GNU/Linux era</label>
									<div class="controls">
									  <label class="checkbox inline">
										<input type="checkbox" id="so" name="so_debian"> Debian
									  </label>
									  <label class="checkbox inline">
										<input type="checkbox" id="so" name="so_centos"> CentOS
									  </label>
									</div>
								  </div>

								<div class="form-group">
									<label class="control-label" for="focusedInput">Nome do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                        Exemplo: apache2
                                        </i></font>
									  <input class="form-control focused" id="p_name" name="p_name" type="text" autocomplete="disabled">
									</div>
                                </div>
								<div class="form-group">
									<label class="control-label" for="focusedInput">UID do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                     Exemplo: 33
                                     </i></font>
									  <input class="form-control focused" id="p_uid" name="p_uid" type="number" autocomplete="disabled">
									</div>
                                </div>
								<div class="form-group">
									<label class="control-label" for="focusedInput">GID do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                     Exemplo: 33
                                     </i></font>
									  <input class="form-control focused" id="p_gid" name="p_gid" type="number" autocomplete="disabled">
									</div>
                                </div>

                                <div class="form-group">
									<label class="control-label" for="focusedInput">Argumentos do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                    Exemplo: -k start --config=/etc/servico/configuracao.conf --log=/tmp/arq.log
                                    </i></font>
									  <input class="form-control focused" id="p_args" name="p_args" type="text" autocomplete="disabled">
									</div>
                                </div>
                                <div class="form-group">
								  <label class="control-label" for="textarea2">Arquivos abertos pelo processo</label>
								  <div class="controls">
                                  <font color="#b8b8b8"><i>
                                    Exemplo:<br>
                                    usuario,grupo,DAC,caminho-completo-para-o-arquivo<br>
                                    root,adm,640,/var/log/apache2/error.log<br>
                                    root,root,644,/var/log/apache2/other_vhosts_access.log<br>
                                    root,adm,640,/var/log/apache2/access.log<br>
                                    </i></font>
									<textarea id="p_io" name="p_io" rows="3" style="width:100%" autocomplete="disabled"></textarea>
								  </div>
								</div>
                                <div class="form-group">
								  <label class="control-label" for="textarea2">Portas abertas pelo processo</label>
								  <div class="controls">
                                    <font color="#b8b8b8"><i>
                                    Exemplo:
                                    protocolo:endereço-ip-utilizado:porta
                                    tcp:0.0.0.0:80,udp:127.0.0.1:68,tcp:127.0.0.2:443
                                    </i></font>
									<textarea id="p_portas" name="p_portas" rows="3" style="width:100%" autocomplete="disabled"></textarea>
								  </div>
								</div>
                                <div class="form-group">
								  <label class="control-label" for="textarea2">Banner(s) do processo</label>
								  <div class="controls">
                                    <font color="#b8b8b8"><i>
                                    protocolo:endereço-ip-utilizado:porta:banner
                                    tcp,0.0.0.0,80,Apache httpd,tcp,0.0.0.0,443,Apache httpd
                                    </i></font>
									<textarea id="p_banners" name="p_banners" rows="3" style="width:100%" autocomplete="disabled"></textarea>
								  </div>
								</div>
                                <div class="form-group">
									<label class="control-label" for="focusedInput">Arquivo executável do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                    Exemplo: /usr/lib/apache2/mpm-prefork/apache2
                                    </i></font>
									  <input class="form-control focused" id="p_file" name="p_file" type="text" autocomplete="disabled">
									</div>
                                </div>
                                <div class="form-group">
									<label class="control-label" for="focusedInput">Pacote a qual pertence o processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                    Exemplo: apache2-2.2.22
                                    </i></font>
									  <input class="form-control focused" id="p_package" name="p_package" type="text" autocomplete="disabled">
									</div>
                                </div>
      
                                <div class="form-group">
									<label class="control-label">Pacote RPM ou DPKG?</label>
									<div class="controls">
									  <label class="checkbox inline">
										<input type="checkbox" id="p_rpm" name="p_rpm" value="rpm"> RPM
									  </label>
									  <label class="checkbox inline">
										<input type="checkbox" id="p_dpkg" name="p_dpkg" value="dpkg"> DPKG
									  </label>
									</div>
								  </div>
                                <div class="form-group">
									<label class="control-label" for="focusedInput">Esquema de permissões DAC do arquivo executável do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                    Exemplo: 755
                                    </i></font>
									  <input class="form-control focused" id="pf_dac" type="number" autocomplete="disabled">
									</div>
                                </div>
                                <div class="form-group">
									<label class="control-label" for="focusedInput">UID do arquivo executável do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                    Exemplo: 0
                                    </i></font>
									  <input class="form-control focused" id="pf_uid" name="pf_uid" type="number" autocomplete="disabled">
									</div>
                                </div>
                                <div class="form-group">
									<label class="control-label" for="focusedInput">GID do arquivo executável do processo</label>
									<div class="controls">
                                    <font color="#b8b8b8"><i>
                                    Exemplo: 0
                                    </i></font>
									  <input class="form-control focused" id="pf_gid" name="pf_gid" type="number" autocomplete="disabled">
									</div>
                                </div>

                                <div class="form-group">
								  <label class="control-label" for="textarea2">Descrição da vulnerabilidade</label>
								  <div class="controls">
                                  <font color="#b8b8b8"><i>
                                  Exemplo:<br>
                                  Existe uma vulnerabilidade que atinge esta versão do serviço.<br>
                                    Maiores detalhes podem ser vistos através do CVE número XXXX-XXXX<br>
                                    </i></font>
									<textarea id="p_banners" name="p_desc" rows="3" style="width:100%" autocomplete="disabled"></textarea>
								  </div>
								</div>
                               <div class="form-group">
								  <label class="control-label" for="textarea2">Solução para a vulnerabilidade</label>
								  <div class="controls">
                                  <font color="#b8b8b8"><i>
                                  Exemplo:<br>
                                  Esta vulnerabilidade pode ser corrigida através do update do pacote em questão.
                                    Também pode ser mitigada através de uma configuração específica, detalhada em x.y.z
                                  </i></font>
									<textarea id="p_banners" name="p_sol" rows="3" style="width:100%" autocomplete="disabled"></textarea>
								  </div>
								</div>
                                <div class="form-actions">
								  <button type="submit" class="btn btn-primary">Salvar</button>
								  <button type="reset" class="btn">Cancel</button>
								</div>
                                
                                
                                
							  </fieldset>
							</form>   

						</div>
					</div>
				</div><!--/col-->

			</div><!--/row-->

			</div>
			<!-- end: Content -->
				
        </div><!--/row-->
		
	</div><!--/container-->
	
	
		
	<footer>
		<p>
			<span style="text-align:left;float:left">V-GATHER > APLICAÇÃO DE METODOLOGIA CBR PARA A IDENTIFICAÇÃO DE VULNERABILIDADES</span>
			<span class="hidden-phone" style="text-align:right;float:right">DOUGLAS S. SANTOS, JÉFERSON C. NOBRE - UNISINOS, 2014</span>
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
	<script src="assets/js/jquery.chosen.min.js"></script>
	<script src="assets/js/jquery.cleditor.min.js"></script>
	<script src="assets/js/jquery.autosize.min.js"></script>
	<script src="assets/js/jquery.placeholder.min.js"></script>
	<script src="assets/js/jquery.maskedinput.min.js"></script>
	<script src="assets/js/jquery.inputlimiter.1.3.1.min.js"></script>
	<script src="assets/js/bootstrap-datepicker.min.js"></script>
	<script src="assets/js/bootstrap-timepicker.min.js"></script>
	<script src="assets/js/moment.min.js"></script>
	<script src="assets/js/daterangepicker.min.js"></script>
	<script src="assets/js/jquery.hotkeys.min.js"></script>
	<script src="assets/js/bootstrap-wysiwyg.min.js"></script>
	<script src="assets/js/bootstrap-colorpicker.min.js"></script>
	
	<!-- theme scripts -->
	<script src="assets/js/custom.min.js"></script>
	<script src="assets/js/core.min.js"></script>
	
	<!-- inline scripts related to this page -->
	<script src="assets/js/pages/form-elements.js"></script>
	
	<!-- end: JavaScript-->
	
</body>
</html>