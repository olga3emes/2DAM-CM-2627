drop database usuarios;
create database usuarios;
use usuarios;
create table usuarios(
    id int unsigned not null auto_increment primary key,
    nombre varchar(256) not null
);

INSERT INTO usuarios.usuarios (id, nombre) VALUES (1, 'Olga')
