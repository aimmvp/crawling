* [토크ON세미나] 7강| T아카데미

### Maraidb 사용 in ubuntu
```
$ mysql -u root -p
```
### MariaDB restart
```
$ service mysql restart
```



* table 만들기
```
create database pythonDB;
```
### Table 생성 DDL
 ```
 CREATE TABLE `tbl_keyword` (
  `keyword` varchar(100) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tbl_crawlingData` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `area` varchar(100) DEFAULT NULL,
  `contents` text DEFAULT NULL,
  `keyword` varchar(100) DEFAULT NULL,
  `regdate` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
```
### MariaDB Tool : DBeaver 사용

### MariaDB 한글
http://applejara.tistory.com/516


tbl_crawlingData
id(int) auto
title varchar(100)
price varchar(100)
area varchar(100)
contents text
keyword varchar(100)
regdate timestamp current_timestamp()
