CREATE DATABASE  IF NOT EXISTS `vgather` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `vgather`;


/*
Navicat MySQL Data Transfer

Source Server         : Dev Mysql (Local)
Source Server Version : 50162
Source Host           : 127.0.0.1:3306
Source Database       : vgahter

Target Server Type    : MYSQL
Target Server Version : 50162
File Encoding         : 65001

Date: 2014-08-27 21:04:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for managed_servers
-- ----------------------------
DROP TABLE IF EXISTS `managed_servers`;
CREATE TABLE `managed_servers` (
  `id` int(11)  NOT NULL AUTO_INCREMENT,
  `ipaddress` varchar(15) DEFAULT NULL,
  `hostname` varchar(255) DEFAULT NULL,
  `created` TIMESTAMP NOT NULL,
  `updated` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of managed_servers
-- ----------------------------

-- ----------------------------
-- Table structure for weight_settings
-- ----------------------------
DROP TABLE IF EXISTS `weight_settings`;
CREATE TABLE `weight_settings` (
  `id` int(11)  NOT NULL AUTO_INCREMENT,
  `weight` FLOAT(5,2),
  `descr` varchar(255),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of weight_settings
-- ----------------------------
INSERT INTO weight_settings (weight,descr) VALUES (5.0,"Exato - Característica Essencial");
INSERT INTO weight_settings (weight,descr) VALUES (5.0,"Alto - Excessivamente Importantes");
INSERT INTO weight_settings (weight,descr) VALUES (3.0,"Médio - Relevante, similaridade intermediária");
INSERT INTO weight_settings (weight,descr) VALUES (1.0,"Baixo - Não muito relevante, grau de similaridade pode ser baixo");
INSERT INTO weight_settings (weight,descr) VALUES (0,"Desabilitado - ");

-- ----------------------------
-- Table structure for status_types
-- ----------------------------
DROP TABLE IF EXISTS `case_match`;
CREATE TABLE `case_match` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` int(11) NOT NULL,
  `descr` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of status_types
-- ----------------------------
INSERT INTO case_match (value,descr) VALUES (30,"Valor obtido em avaliação comportamental");

-- ----------------------------
-- Table structure for status_types
-- ----------------------------
DROP TABLE IF EXISTS `status_types`;
CREATE TABLE `status_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of status_types
-- ----------------------------
INSERT INTO status_types VALUES (1,"Caso");
INSERT INTO status_types VALUES (2,"Candidato");

-- ----------------------------
-- Table structure for status_types
-- ----------------------------
DROP TABLE IF EXISTS `origem_types`;
CREATE TABLE `origem_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of status_types
-- ----------------------------
INSERT INTO origem_types VALUES (1,"Registrado");
INSERT INTO origem_types VALUES (2,"Aprendido");

-- ----------------------------
-- Table structure for package_types
-- ----------------------------
DROP TABLE IF EXISTS `package_types`;
CREATE TABLE `package_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of package_types
-- ----------------------------
INSERT INTO package_types (id,name) VALUES (1,"DPKG");
INSERT INTO package_types (id,name) VALUES (2,"RPM");


-- ----------------------------
-- Table structure for sos
-- ----------------------------
DROP TABLE IF EXISTS `sos`;
CREATE TABLE `sos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sos
-- ----------------------------
INSERT INTO sos (id,name) VALUES (1,"Debian");
INSERT INTO sos (id,name) VALUES (2,"CentOS");

-- ----------------------------
-- Table structure for use_cases
-- ja coloquei os pesos.
-- falta melhorar a questao das portas usadas (proto:ip:port)
-- ----------------------------
DROP TABLE IF EXISTS `use_cases`;
CREATE TABLE `use_cases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` TIMESTAMP NOT NULL,
  `status` int NOT NULL,
  `origem` int NOT NULL,
  `case_id_related` int, 
  `so_id` int(11) DEFAULT NULL,
  `so_id_weight` FLOAT(5,2) DEFAULT NULL,
  `so_id_score` FLOAT(5,2) DEFAULT NULL,
  `so_version` varchar(30) DEFAULT NULL,
  `so_version_weight` FLOAT(5,2) DEFAULT NULL,
  `so_version_score` FLOAT(5,2) DEFAULT NULL,
  `process_name` varchar(50) DEFAULT NULL,
  `process_name_weight` FLOAT(5,2) DEFAULT NULL,
  `process_name_score` FLOAT(5,2) DEFAULT NULL,
  `process_uid` int DEFAULT NULL,
  `process_uid_weight` FLOAT(5,2) DEFAULT NULL,
  `process_uid_score` FLOAT(5,2) DEFAULT NULL,
  `process_gid` int DEFAULT NULL,
  `process_gid_weight` FLOAT(5,2) DEFAULT NULL,
  `process_gid_score` FLOAT(5,2) DEFAULT NULL,
  `process_args` varchar(50000) DEFAULT NULL,
  `process_args_weight` FLOAT(5,2) DEFAULT NULL,
  `process_args_score` FLOAT(5,2) DEFAULT NULL,
  `process_tcp_banner` varchar(50000) DEFAULT NULL,
  `process_tcp_banner_weight` FLOAT(5,2) DEFAULT NULL,
  `process_tcp_banner_score` FLOAT(5,2) DEFAULT NULL,
  `process_udp_banner` varchar(50000) DEFAULT NULL,
  `process_udp_banner_weight` FLOAT(5,2) DEFAULT NULL,
  `process_udp_banner_score` FLOAT(5,2) DEFAULT NULL,
  `package_name` varchar(120) DEFAULT NULL,
  `package_name_weight` FLOAT(5,2) DEFAULT NULL,
  `package_name_score` FLOAT(5,2) DEFAULT NULL,
  `package_type_id` int(11) DEFAULT NULL,
  `package_type_id_weight` FLOAT(5,2) DEFAULT NULL,
  `package_type_id_score` FLOAT(5,2) DEFAULT NULL,
  `process_binary` varchar(300) DEFAULT NULL,
  `process_binary_weight` FLOAT(5,2) DEFAULT NULL,
  `process_binary_score` FLOAT(5,2) DEFAULT NULL,
  `process_binary_uid` int DEFAULT NULL,
  `process_binary_uid_weight` FLOAT(5,2) DEFAULT NULL,
  `process_binary_uid_score` FLOAT(5,2) DEFAULT NULL,
  `process_binary_gid` int DEFAULT NULL,
  `process_binary_gid_weight` FLOAT(5,2) DEFAULT NULL,
  `process_binary_gid_score` FLOAT(5,2) DEFAULT NULL,
  `process_binary_dac` int DEFAULT NULL,
  `process_binary_dac_weight` FLOAT(5,2) DEFAULT NULL,
  `process_binary_dac_score` FLOAT(5,2) DEFAULT NULL,
  `candidate_final_score` FLOAT(5,2),
  PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of use_cases
-- ----------------------------
INSERT INTO `use_cases` VALUES (1,'2014-10-02 17:13:23',1,1,NULL,2,5.00,NULL,'6.5',1.00,NULL,'httpd',5.00,NULL,48,1.00,NULL,48,1.00,NULL,'',0.00,NULL,'80:Apache httpd',5.00,NULL,'',0.00,NULL,'httpd-2.2.15',5.00,NULL,NULL,NULL,NULL,'/usr/sbin/httpd',1.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);


-- ----------------------------
-- Table structure for use_case_desc_solution
-- ----------------------------
DROP TABLE IF EXISTS `use_case_desc_solution`;
CREATE TABLE `use_case_desc_solution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` int(11) DEFAULT NULL,
  `description` varchar(10000) DEFAULT NULL,
  `solution` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of use_case_desc_solution
-- ----------------------------

INSERT INTO `use_case_desc_solution` VALUES (1,1,'O Apache sofre de uma vulnerabilidade x,y,z.','Para solucionar, Ã© preciso aplicar as recomendaÃ§Ãµes de hardening do documento xyzw');


-- ----------------------------
-- Table structure for mgr_login_attempts
-- ----------------------------
DROP TABLE IF EXISTS `mgr_login_attempts`;
CREATE TABLE `mgr_login_attempts` (
    `user_id` INT(11) NOT NULL,
    `time` VARCHAR(30) NOT NULL
) ENGINE=InnoDB;
-- ----------------------------
-- Table structure for mgr_login_attempts
-- ----------------------------

-- ----------------------------
-- Table structure for mgr_users
-- ----------------------------

DROP TABLE IF EXISTS `mgr_users`;
CREATE TABLE `mgr_users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(30) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `password` CHAR(128) NOT NULL,
    `salt` CHAR(128) NOT NULL 
) ENGINE = InnoDB;

-- -----------
-- default creds:
--  usuario: vmgr
--  email: vmgr@teste.com
--  senha: 6ZaxN2Vzm9NUJT2y
-- -----------
INSERT INTO mgr_users VALUES(1, 'vmgr', 'vmgr@teste.com',
'00807432eae173f652f2064bdca1b61b290b52d40e429a7d295d76a71084aa96c0233b82f1feac45529e0726559645acaed6f3ae58a286b9f075916ebf66cacc',
'f9aab579fc1b41ed0c44fe4ecdbfcdb4cb99b9023abb241a6db833288f4eea3c02f76e0d35204a8695077dcf81932aa59006423976224be0390395bae152d4ef');


