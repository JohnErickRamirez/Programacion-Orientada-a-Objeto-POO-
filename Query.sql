create database bd1;
use bd1;

create table articulos(
	codigo int primary key auto_increment,
    descripcion varchar(50),
    precio float
);

select * from articulos;
