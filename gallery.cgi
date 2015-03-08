#!/usr/bin/perl -w
use CGI qw(:standard);
use diagnostics;
use CGI::Carp 'fatalsToBrowser';
use Config::Simple;
use DBI;

my $cfg = new Config::Simple('images.config');
my $author = $cfg->param("site.author");
my $title = $cfg->param("site.title");
my $dsn = $cfg->param("mysql.dsn");
my $user = $cfg->param("mysql.user");
my $password = $cfg->param("mysql.password");
my $dbh = DBI->connect($dsn, $user, $password) or die;
my $sth = $dbh->prepare("SELECT * FROM Image");

print header;

print "<head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />
<title>$title</title>
<link rel=\"stylesheet\" type=\"text/css\" href=\"css/styles.css\" />
<link href='http://fonts.googleapis.com/css?family=Cambo' rel='stylesheet' type='text/css'>
<script src=\"http://code.jquery.com/jquery-latest.js\"></script>
<script src=\"js/image.js\"></script>
<!--[if IE]><script src=\"http://html5shiv.googlecode.com/svn/trunk/html5.js\"></script><![endif]-->
</head>
<body onload=\"setupBlocks();\">";
 $sth->execute();
while (my $ref = $sth->fetchrow_hashref()) {

print "<div class=\"block\">";
print "<p><a href='image.cgi?UUID=$ref->{'ImageUUID'}'><img src='thumbnail.cgi?UUID=$ref->{'ImageUUID'}' width=\"259\"/></a></p>";
print "</div>";
	
}