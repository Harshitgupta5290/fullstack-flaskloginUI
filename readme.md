Here is the method to see how to create database in mysql and used in flask

CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY_KEY (userid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

because of the table user is created now insert some values if u want and for that 
use the following code:

INSERT INTO user (name, email, password) VALUES ('your name','your email', 'your password');

