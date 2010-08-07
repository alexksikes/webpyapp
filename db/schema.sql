# Make sure the database is UTF-8 (needed for load data infile)
create database if not exists demo default charset utf8; use demo;

drop table if exists demo_table;
create table demo_table (
    id                              int(32) unsigned primary key,
    name                            varchar(250) not null
) charset utf8;