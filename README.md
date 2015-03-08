# furry-ninja
This is a work in progress image gallary writen in php/perl using a mysql database as a backend.

As of right now you can hard code all the images I have it set up so that if you wanted to have the images some were not accessable to the web site but accessable to perl you can by setting `$BaseDir` in each cgi.

## To-DO
* *Database*
* Config File
* Gallery page
* Upload area
* Albums
* User auth/ACL
* Image page (more info and such)

## Config File
Here is what I have going for the config file so far. (also in images.config.example)

```
[site]
title="Simple Perl Gallery"
author=srainsdon

[mysql]  
dsn="dbi:mysql:<ImageDB>;host=<DBHost>"
user=<DBUser>
password=<DBPassword>
```
