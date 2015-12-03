/*
Navicat MySQL Data Transfer

Source Server         : vmware
Source Server Version : 50542
Source Host           : 192.168.1.203:3306
Source Database       : static

Target Server Type    : MYSQL
Target Server Version : 50542
File Encoding         : 65001

Date: 2015-09-23 19:29:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for xls_table_map
-- ----------------------------
DROP TABLE IF EXISTS `xls_table_map`;
CREATE TABLE `xls_table_map` (
  `xls_name` varchar(255) NOT NULL,
  `table_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`xls_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
