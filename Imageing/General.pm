package General;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);
use Config::Simple;
use DBI;

my $VERSION     = 1.00;
my @ISA         = qw(Exporter);
my @EXPORT      = ();
my @EXPORT_OK   = qw(&new &getImageList &getTitle);
my %EXPORT_TAGS = ( DEFAULT => [qw(&new &getImageList &getTitle)],
                 Both    => [qw(&new &func2)]);

use Log::Log4perl;

our $logger;
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
    Log::Log4perl::init($cfg->param("config.logging"));
	$logger = Log::Log4perl->get_logger('General');
	$logger->debug("Logging Started:");
    setupDB();
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
	$logger->debug("Rows Selected: $numRows");
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