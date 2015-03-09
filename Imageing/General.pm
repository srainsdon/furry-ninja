package General;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);
use Config::Simple;
use DBI;

my $VERSION     = 1.00;
my @ISA         = qw(Exporter);
my @EXPORT      = ();
my @EXPORT_OK   = qw(&new &getImageList);
my %EXPORT_TAGS = ( DEFAULT => [qw(&new &getImageList)],
                 Both    => [qw(&new &func2)]);

our $cfg;
our $author;
our $title;
our $dsn;
our $user;
our $password;
our $dbh;

sub getTitle
{
	return $title;
}

sub new
{
    my $class = shift;
    my $self = {
        _configfile => shift,
    };
    $cfg = new Config::Simple("$self->{_configfile}");
    #print "Config File is $self->{_configfile}\n";
    setupDB();
    # Print all the values just for clarification.
    #print "Site Info:\nAuthor: $author\nTitle: $title\n";
    bless $self, $class;
    return $self;
}

sub setupDB
{
	$author = $cfg->param("site.author");
	$title = $cfg->param("site.title");
	$dsn = $cfg->param("mysql.dsn");
	$user = $cfg->param("mysql.user");
	$password = $cfg->param("mysql.password");
	$dbh = DBI->connect($dsn, $user, $password) or die;
}

sub getImageList
{
	my $sth = $dbh->prepare("SELECT * FROM Image");
	$sth->execute();
	my $numRows = $sth->rows;
	my $x = 0;
	my @DBInfo;
	while ($x < $numRows)
	{
		$DBInfo[$x] = $sth->fetchrow_hashref();
		# print $DBInfo[$x] . "\n";
		$x++;
	}
	return @DBInfo;
}

1;