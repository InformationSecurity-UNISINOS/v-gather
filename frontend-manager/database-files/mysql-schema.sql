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
-- Table structure for status_types
-- ----------------------------
DROP TABLE IF EXISTS `case_match`;
CREATE TABLE `case_match` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` int(11) NOT NULL DEFAULT 6,
  `desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of status_types
-- ----------------------------


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
INSERT INTO sos (id,name) VALUES (1,"debian");
INSERT INTO sos (id,name) VALUES (2,"centos");

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
  `so_id_weight` FLOAT(3,2) DEFAULT NULL,
  `so_version` varchar(30) DEFAULT NULL,
  `so_version_weight` FLOAT(3,2) DEFAULT NULL,
  `process_name` varchar(50) DEFAULT NULL,
  `process_name_weight` FLOAT(3,2) DEFAULT NULL,
  `process_uid` int DEFAULT NULL,
  `process_uid_weight` FLOAT(3,2) DEFAULT NULL,
  `process_gid` int DEFAULT NULL,
  `process_gid_weight` FLOAT(3,2) DEFAULT NULL,
  `process_args` varchar(50000) DEFAULT NULL,
  `process_args_weight` FLOAT(3,2) DEFAULT NULL,
  `process_tcp_banner` varchar(50000) DEFAULT NULL,
  `process_tcp_banner_weight` FLOAT(3,2) DEFAULT NULL,
  `process_udp_banner` varchar(50000) DEFAULT NULL,
  `process_udp_banner_weight` FLOAT(3,2) DEFAULT NULL,
  `package_name` varchar(120) DEFAULT NULL,
  `package_name_weight` FLOAT(3,2) DEFAULT NULL,
  `package_type_id` int(11) DEFAULT NULL,
  `package_type_id_weight` FLOAT(3,2) DEFAULT NULL,
  `process_binary` varchar(300) DEFAULT NULL,
  `process_binary_weight` FLOAT(3,2) DEFAULT NULL,
  `process_binary_uid` int DEFAULT NULL,
  `process_binary_uid_weight` FLOAT(3,2) DEFAULT NULL,
  `process_binary_gid` int DEFAULT NULL,
  `process_binary_gid_weight` FLOAT(3,2) DEFAULT NULL,
  `process_binary_dac` int DEFAULT NULL,
  `process_binary_dac_weight` FLOAT(3,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `so_id` (`so_id`),
  KEY `package_type_id` (`package_type_id`),
  CONSTRAINT `use_cases_ibfk_2` FOREIGN KEY (`package_type_id`) REFERENCES `package_types` (`id`) ON DELETE CASCADE,
  CONSTRAINT `use_cases_ibfk_1` FOREIGN KEY (`so_id`) REFERENCES `sos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of use_cases
-- ----------------------------


-- ----------------------------
-- Table structure for use_case_desc_solution
-- ----------------------------
DROP TABLE IF EXISTS `use_case_desc_solution`;
CREATE TABLE `use_case_desc_solution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` int(11) DEFAULT NULL,
  `description` varchar(10000) DEFAULT NULL,
  `solution` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `case_id` (`case_id`),
  CONSTRAINT `use_case_desc_solution_ibfk_1` FOREIGN KEY (`case_id`) REFERENCES `use_cases` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of use_case_desc_solution
-- ----------------------------




-- ----------------------------
-- Table structure for mgr_users
-- ----------------------------
CREATE TABLE `mgr_users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(30) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `password` CHAR(128) NOT NULL,
    `salt` CHAR(128) NOT NULL 
) ENGINE = InnoDB;
-- ----------------------------
-- Table structure for mgr_users
-- ----------------------------


-- ----------------------------
-- Table structure for mgr_login_attempts
-- ----------------------------
CREATE TABLE `mgr_login_attempts` (
    `user_id` INT(11) NOT NULL,
    `time` VARCHAR(30) NOT NULL
) ENGINE=InnoDB;
-- ----------------------------
-- Table structure for mgr_login_attempts
-- ----------------------------


-- -----------
-- default creds:
--  usuario: vmgr
--  email: vmgr@teste.com
--  senha: 6ZaxN2Vzm9NUJT2y
-- -----------
INSERT INTO mgr_users VALUES(1, 'vmgr', 'vmgr@teste.com',
'00807432eae173f652f2064bdca1b61b290b52d40e429a7d295d76a71084aa96c0233b82f1feac45529e0726559645acaed6f3ae58a286b9f075916ebf66cacc',
'f9aab579fc1b41ed0c44fe4ecdbfcdb4cb99b9023abb241a6db833288f4eea3c02f76e0d35204a8695077dcf81932aa59006423976224be0390395bae152d4ef');



