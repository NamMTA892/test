create database IF NOT EXISTS myDB;

use myDB;

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
);

INSERT INTO `users` (`id`, `username`, `password`) VALUES (1, 'admin', MD5('Honghanh@2501'));