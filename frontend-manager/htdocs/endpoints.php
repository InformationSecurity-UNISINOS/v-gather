
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
			
			
			<div class="row">		
				<div class="col-sm-12 col-md-12">
					<div class="box">
						<div class="box-header" data-original-title>
							<h2><i class="fa fa-user"></i><span class="break"></span>Members</h2>
							<div class="box-icon">
								<a href="table.html#" class="btn-setting"><i class="fa fa-wrench"></i></a>
								<a href="table.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>
								<a href="table.html#" class="btn-close"><i class="fa fa-times"></i></a>
							</div>
						</div>
						<div class="box-content">
							<table class="table table-striped table-bordered bootstrap-datatable datatable">
							  <thead>
								  <tr>
									  <th>Username</th>
									  <th>Date registered</th>
									  <th>Role</th>
									  <th>Status</th>
									  <th>Actions</th>
								  </tr>
							  </thead>   
							  <tbody>
								<tr>
									<td>Anton Phunihel</td>
									<td>2012/01/01</td>
									<td>Member</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>  
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>  
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Alphonse Ivo</td>
									<td>2012/01/01</td>
									<td>Member</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>  
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>  
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Thancmar Theophanes</td>
									<td>2012/01/01</td>
									<td>Member</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>  
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>  
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
									</td>
								</tr>
								<tr>
									<td>Walerian Khwaja</td>
									<td>2012/01/01</td>
									<td>Member</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Clemens Janko</td>
									<td>2012/02/01</td>
									<td>Staff</td>
									<td>
										<span class="label label-important">Banned</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Chidubem Gottlob</td>
									<td>2012/02/01</td>
									<td>Staff</td>
									<td>
										<span class="label label-important">Banned</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Hristofor Sergio</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Tadhg Griogair</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Pollux Beaumont</td>
									<td>2012/01/21</td>
									<td>Staff</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Adam Alister</td>
									<td>2012/01/21</td>
									<td>Staff</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Carlito Roffe</td>
									<td>2012/08/23</td>
									<td>Staff</td>
									<td>
										<span class="label label-important">Banned</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Sana Amrin</td>
									<td>2012/08/23</td>
									<td>Staff</td>
									<td>
										<span class="label label-important">Banned</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Adinah Ralph</td>
									<td>2012/06/01</td>
									<td>Admin</td>
									<td>
										<span class="label label-default">Inactive</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Dederick Mihail</td>
									<td>2012/06/01</td>
									<td>Admin</td>
									<td>
										<span class="label label-default">Inactive</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 
										</a>
									</td>
								</tr>
								<tr>
									<td>Hipólito András</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Fricis Arieh</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Scottie Maximilian</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Bao Gaspar</td>
									<td>2012/01/01</td>
									<td>Member</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Tullio Luka</td>
									<td>2012/02/01</td>
									<td>Staff</td>
									<td>
										<span class="label label-important">Banned</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Felice Arseniy</td>
									<td>2012/02/01</td>
									<td>Admin</td>
									<td>
										<span class="label label-default">Inactive</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Finlay Alf</td>
									<td>2012/02/01</td>
									<td>Admin</td>
									<td>
										<span class="label label-default">Inactive</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Theophilus Nala</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Sullivan Robert</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Kristóf Filiberto</td>
									<td>2012/01/21</td>
									<td>Staff</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Kuzma Edvard</td>
									<td>2012/01/21</td>
									<td>Staff</td>
									<td>
										<span class="label label-success">Active</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Bünyamin Kasper</td>
									<td>2012/08/23</td>
									<td>Staff</td>
									<td>
										<span class="label label-important">Banned</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Crofton Arran</td>
									<td>2012/08/23</td>
									<td>Staff</td>
									<td>
										<span class="label label-important">Banned</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Bernhard Shelah</td>
									<td>2012/06/01</td>
									<td>Admin</td>
									<td>
										<span class="label label-default">Inactive</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Grahame Miodrag</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Innokentiy Celio</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Kostandin Warinhari</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
								<tr>
									<td>Ajith Hristijan</td>
									<td>2012/03/01</td>
									<td>Member</td>
									<td>
										<span class="label label-warning">Pending</span>
									</td>
									<td>
										<a class="btn btn-success" href="table.html#">
											<i class="fa fa-search-plus "></i>                                            
										</a>
										<a class="btn btn-info" href="table.html#">
											<i class="fa fa-edit "></i>                                            
										</a>
										<a class="btn btn-danger" href="table.html#">
											<i class="fa fa-trash-o "></i> 

										</a>
									</td>
								</tr>
							  </tbody>
						  </table>            
						</div>
					</div>
				</div><!--/col-->
			
			</div><!--/row-->

			<div class="row">
				<div class="col-lg-6">
					<div class="box">
						<div class="box-header">
							<h2><i class="fa fa-align-justify"></i><span class="break"></span>Simple Table</h2>
							<div class="box-icon">
								<a href="table.html#" class="btn-setting"><i class="fa fa-wrench"></i></a>
								<a href="table.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>
								<a href="table.html#" class="btn-close"><i class="fa fa-times"></i></a>
							</div>
						</div>
						<div class="box-content">
							<table class="table">
								  <thead>
									  <tr>
										  <th>Username</th>
										  <th>Date registered</th>
										  <th>Role</th>
										  <th>Status</th>                                          
									  </tr>
								  </thead>   
								  <tbody>
									<tr>
										<td>Samppa Nori</td>
										<td>2012/01/01</td>
										<td>Member</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                       
									</tr>
									<tr>
										<td>Estavan Lykos</td>
										<td>2012/02/01</td>
										<td>Staff</td>
										<td>
											<span class="label label-important">Banned</span>
										</td>                                       
									</tr>
									<tr>
										<td>Chetan Mohamed</td>
										<td>2012/02/01</td>
										<td>Admin</td>
										<td>
											<span class="label label-default">Inactive</span>
										</td>                                        
									</tr>
									<tr>
										<td>Derick Maximinus</td>
										<td>2012/03/01</td>
										<td>Member</td>
										<td>
											<span class="label label-warning">Pending</span>
										</td>                                       
									</tr>
									<tr>
										<td>Friderik Dávid</td>
										<td>2012/01/21</td>
										<td>Staff</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                        
									</tr>                                   
								  </tbody>
							 </table>  
							 <div class="pagination pagination-centered">
							  <ul class="pagination">
								<li><a href="table.html#">Prev</a></li>
								<li class="active">
								  <a href="table.html#">1</a>
								</li>
								<li><a href="table.html#">2</a></li>
								<li><a href="table.html#">3</a></li>
								<li><a href="table.html#">4</a></li>
								<li><a href="table.html#">Next</a></li>
							  </ul>
							</div>     
						</div>
					</div>
				</div><!--/col-->
				
				<div class="col-lg-6">
					<div class="box">
						<div class="box-header">
							<h2><i class="fa fa-align-justify"></i><span class="break"></span>Striped Table</h2>
							<div class="box-icon">
								<a href="table.html#" class="btn-setting"><i class="fa fa-wrench"></i></a>
								<a href="table.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>
								<a href="table.html#" class="btn-close"><i class="fa fa-times"></i></a>
							</div>
						</div>
						<div class="box-content">
							<table class="table table-striped">
								  <thead>
									  <tr>
										  <th>Username</th>
										  <th>Date registered</th>
										  <th>Role</th>
										  <th>Status</th>                                          
									  </tr>
								  </thead>   
								  <tbody>
									<tr>
										<td>Yiorgos Avraamu</td>
										<td>2012/01/01</td>
										<td>Member</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                       
									</tr>
									<tr>
										<td>Avram Tarasios</td>
										<td>2012/02/01</td>
										<td>Staff</td>
										<td>
											<span class="label label-important">Banned</span>
										</td>                                       
									</tr>
									<tr>
										<td>Quintin Ed</td>
										<td>2012/02/01</td>
										<td>Admin</td>
										<td>
											<span class="label label-default">Inactive</span>
										</td>                                        
									</tr>
									<tr>
										<td>Enéas Kwadwo</td>
										<td>2012/03/01</td>
										<td>Member</td>
										<td>
											<span class="label label-warning">Pending</span>
										</td>                                       
									</tr>
									<tr>
										<td>Agapetus Tadeáš</td>
										<td>2012/01/21</td>
										<td>Staff</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                        
									</tr>                                   
								  </tbody>
							 </table>  
							 <div class="pagination pagination-centered">
							  <ul class="pagination">
								<li><a href="table.html#">Prev</a></li>
								<li class="active">
								  <a href="table.html#">1</a>
								</li>
								<li><a href="table.html#">2</a></li>
								<li><a href="table.html#">3</a></li>
								<li><a href="table.html#">4</a></li>
								<li><a href="table.html#">Next</a></li>
							  </ul>
							</div>     
						</div>
					</div>
				</div><!--/col-->
			</div><!--/row-->
			
			<div class="row">
				
				<div class="col-lg-6">
					<div class="box">
						<div class="box-header">
							<h2><i class="fa fa-align-justify"></i><span class="break"></span>Condensed Table</h2>
							<div class="box-icon">
								<a href="table.html#" class="btn-setting"><i class="fa fa-wrench"></i></a>
								<a href="table.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>
								<a href="table.html#" class="btn-close"><i class="fa fa-times"></i></a>
							</div>
						</div>
						<div class="box-content">
							<table class="table table-condensed">
								  <thead>
									  <tr>
										  <th>Username</th>
										  <th>Date registered</th>
										  <th>Role</th>
										  <th>Status</th>                                          
									  </tr>
								  </thead>   
								  <tbody>
									<tr>
										<td>Carwyn Fachtna</td>
										<td>2012/01/01</td>
										<td>Member</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                       
									</tr>
									<tr>
										<td>Nehemiah Tatius</td>
										<td>2012/02/01</td>
										<td>Staff</td>
										<td>
											<span class="label label-important">Banned</span>
										</td>                                       
									</tr>
									<tr>
										<td>Ebbe Gemariah</td>
										<td>2012/02/01</td>
										<td>Admin</td>
										<td>
											<span class="label label-default">Inactive</span>
										</td>                                        
									</tr>
									<tr>
										<td>Eustorgios Amulius</td>
										<td>2012/03/01</td>
										<td>Member</td>
										<td>
											<span class="label label-warning">Pending</span>
										</td>                                       
									</tr>
									<tr>
										<td>Leopold Gáspár</td>
										<td>2012/01/21</td>
										<td>Staff</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                        
									</tr>                                   
								  </tbody>
							 </table>  
							 <div class="pagination pagination-centered">
							  <ul class="pagination">
								<li><a href="table.html#">Prev</a></li>
								<li class="active">
								  <a href="table.html#">1</a>
								</li>
								<li><a href="table.html#">2</a></li>
								<li><a href="table.html#">3</a></li>
								<li><a href="table.html#">4</a></li>
								<li><a href="table.html#">Next</a></li>
							  </ul>
							</div>     
						</div>
					</div>
				</div><!--/col-->
					
				<div class="col-lg-6">
					<div class="box">
						<div class="box-header">
							<h2><i class="fa fa-align-justify"></i><span class="break"></span>Bordered Table</h2>
							<div class="box-icon">
								<a href="table.html#" class="btn-setting"><i class="fa fa-wrench"></i></a>
								<a href="table.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>
								<a href="table.html#" class="btn-close"><i class="fa fa-times"></i></a>
							</div>
						</div>
						<div class="box-content">
							<table class="table table-bordered">
								  <thead>
									  <tr>
										  <th>Username</th>
										  <th>Date registered</th>
										  <th>Role</th>
										  <th>Status</th>                                          
									  </tr>
								  </thead>   
								  <tbody>
									<tr>
										<td>Pompeius René</td>
										<td>2012/01/01</td>
										<td>Member</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                       
									</tr>
									<tr>
										<td>Paĉjo Jadon</td>
										<td>2012/02/01</td>
										<td>Staff</td>
										<td>
											<span class="label label-important">Banned</span>
										</td>                                       
									</tr>
									<tr>
										<td>Micheal Mercurius</td>
										<td>2012/02/01</td>
										<td>Admin</td>
										<td>
											<span class="label label-default">Inactive</span>
										</td>                                        
									</tr>
									<tr>
										<td>Ganesha Dubhghall</td>
										<td>2012/03/01</td>
										<td>Member</td>
										<td>
											<span class="label label-warning">Pending</span>
										</td>                                       
									</tr>
									<tr>
										<td>Hiroto Šimun</td>
										<td>2012/01/21</td>
										<td>Staff</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                        
									</tr>                                   
								  </tbody>
							 </table>  
							 <ul class="pagination">
								<li><a href="table.html#">Prev</a></li>
								<li class="active">
								  <a href="table.html#">1</a>
								</li>
								<li><a href="table.html#">2</a></li>
								<li><a href="table.html#">3</a></li>
								<li><a href="table.html#">4</a></li>
								<li><a href="table.html#">Next</a></li>
							 </ul>
						</div>
					</div>
				</div><!--/col-->
			
			</div><!--/row-->
			
			<div class="row">	
				<div class="col-lg-12">
					<div class="box">
						<div class="box-header">
							<h2><i class="fa fa-align-justify"></i><span class="break"></span>Combined All Table</h2>
							<div class="box-icon">
								<a href="table.html#" class="btn-setting"><i class="fa fa-wrench"></i></a>
								<a href="table.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>
								<a href="table.html#" class="btn-close"><i class="fa fa-times"></i></a>
							</div>
						</div>
						<div class="box-content">
							<table class="table table-bordered table-striped table-condensed">
								  <thead>
									  <tr>
										  <th>Username</th>
										  <th>Date registered</th>
										  <th>Role</th>
										  <th>Status</th>                                          
									  </tr>
								  </thead>   
								  <tbody>
									<tr>
										<td>Vishnu Serghei</td>
										<td>2012/01/01</td>
										<td>Member</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                       
									</tr>
									<tr>
										<td>Zbyněk Phoibos</td>
										<td>2012/02/01</td>
										<td>Staff</td>
										<td>
											<span class="label label-important">Banned</span>
										</td>                                       
									</tr>
									<tr>
										<td>Einar Randall</td>
										<td>2012/02/01</td>
										<td>Admin</td>
										<td>
											<span class="label label-default">Inactive</span>
										</td>                                        
									</tr>
									<tr>
										<td>Félix Troels</td>
										<td>2012/03/01</td>
										<td>Member</td>
										<td>
											<span class="label label-warning">Pending</span>
										</td>                                       
									</tr>
									<tr>
										<td>Aulus Agmundr</td>
										<td>2012/01/21</td>
										<td>Staff</td>
										<td>
											<span class="label label-success">Active</span>
										</td>                                        
									</tr>                                   
								  </tbody>
							 </table>  
							 <div class="pagination pagination-centered">
							  <ul class="pagination">
								<li><a href="table.html#">Prev</a></li>
								<li class="active">
								  <a href="table.html#">1</a>
								</li>
								<li><a href="table.html#">2</a></li>
								<li><a href="table.html#">3</a></li>
								<li><a href="table.html#">4</a></li>
								<li><a href="table.html#">Next</a></li>
							  </ul>
							</div>     
						</div>
					</div>
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
			<span style="text-align:left;float:left">&copy; 2013 creativeLabs. <a href="http://bootstrapmaster.com">Admin Templates</a> by BootstrapMaster</span>
			<span class="hidden-phone" style="text-align:right;float:right">Powered by: <a href="http://bootstrapmaster.com/demo/genius/" alt="Bootstrap Admin Templates">Genius Dashboard</a></span>
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