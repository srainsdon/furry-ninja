#!/usr/bin/perl -w
use CGI qw(:standard);
use diagnostics;
use CGI::Carp 'fatalsToBrowser';
use Imageing::General;
$gen = new General( "images.config" );


print header;

print "<head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />
<title>" . $gen->getTitle() . "</title>
<link rel=\"stylesheet\" type=\"text/css\" href=\"css/styles.css\" />
<link href='http://fonts.googleapis.com/css?family=Cambo' rel='stylesheet' type='text/css'>
<script src=\"http://code.jquery.com/jquery-latest.js\"></script>
<script src=\"js/image.js\"></script>
<!--[if IE]><script src=\"http://html5shiv.googlecode.com/svn/trunk/html5.js\"></script><![endif]-->
</head>
<body onload=\"setupBlocks();\">\n";
@List = $gen->getImageList();
foreach my $ref (keys @List) {
print "<div class=\"block\">";
print "<p><a href='image.cgi?UUID=" . @List[$ref]->{'ImageUUID'} . "'>";
print "<h6>" . @List[$ref]->{'ImageName'} . "</h6><img src='thumbnail.cgi?UUID=" . @List[$ref]->{'ImageUUID'} . "' width=\"259\"/></a>";
print @List[$ref]->{'ImageDescription'} . "</p>";
print "</div>\n";
	
}
print "</body></html>";