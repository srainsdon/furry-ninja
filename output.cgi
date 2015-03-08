#!/usr/bin/perl -w
use CGI qw(:standard);
use XML::Writer;
use diagnostics;
use CGI::Carp 'fatalsToBrowser';
use Config::Simple;

my $cfg = new Config::Simple('images.config');
my $author = $cfg->param("site.author");
my $title = $cfg->param("site.title");
my $dsn = $cfg->param("mysql.dsn");
my $user = $cfg->param("mysql.user");
my $password = $cfg->param("mysql.password");

use DBI;

    $dbh = DBI->connect($dsn, $user, $password) or die;
my $sth = $dbh->prepare("SELECT * FROM Image");

my $output = '';
my $writer = XML::Writer->new(
    OUTPUT      => \$output,
    DATA_MODE   => 1,
    DATA_INDENT => 1
);
$writer->xmlDecl('UTF-8');
$writer->startTag('response');
  $sth->execute();
  while (my $ref = $sth->fetchrow_hashref()) {
	$writer->startTag( 'image' );
	$writer->startTag( 'ID' );
	$writer->characters($ref->{'ImageID'});
	$writer->endTag( 'ID' );
	$writer->startTag( 'UUID' );
	$writer->characters($ref->{'ImageUUID'});
	$writer->endTag( 'UUID' );
	$writer->startTag( 'Name' );
	$writer->characters($ref->{'ImageName'});
	$writer->endTag( 'Name' );
	$writer->startTag( 'Description' );
	$writer->characters($ref->{'ImageDescription'});
	$writer->endTag( 'Description' );
	$writer->endTag( 'image' );
    # ImageDescription "Found a row: id = $ref->{'id'}, name = $ref->{'name'}\n";
  }
  $sth->finish();
$writer->endTag('response');
$writer->end();

print header('text/xml'), $output;

1;
