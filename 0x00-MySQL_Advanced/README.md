# MySQL advanced

## Description
> This repository contains files that are created for an deeped and advanced understanding of MySQL concepts such as optimisation using indexes, implementation of views, triggers, stored procedures,  and functions in MySQL.

## Requirements
- OS: `Ubuntu 18.04 LTS`
- Language(s): `MySQL` (version 5.7.3)
- Linter: `None`
- Editors: `vi`, `emacs`

## How to start my SQL
```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password:
Database
information_schema
mysql
performance_schema
sys
$
```

## How to import MySQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Author
- Siphamandla Matshiane, ![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2FSiphamandl76892)
