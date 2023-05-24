CREATE DATABASE `project-6497366e-35e4-4290-bef1-071ba59ed974` CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE `project-default` CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER root IDENTIFIED BY 'pwd123456';
GRANT All privileges ON *.* TO root@'%';
flush privileges;
