#!/usr/bin/perl -w

use strict;
use CGI;
use diagnostics;
use CGI::Carp 'fatalsToBrowser';
use Log::Log4perl;
Log::Log4perl::init('/home/Hosting/Sites/images.247ly.com/Config/logging.conf');
my $logger = Log::Log4perl->get_logger('Image');

my $BaseDir = "/var/www/images";

my $q = CGI->new();
#my $UUID = '8f89785f-d9a9-4663-8aa6-592c3b053a1a';
my $UUID = $q->param('UUID');
$logger->debug("UUID: $UUID");
my $filename = "$BaseDir/$UUID.jpg";
my $TNfilename = "$BaseDir/thumbnails/$UUID.jpg";
$logger->debug("Thumbnail File Name: $TNfilename");

unless (-e $TNfilename) {
use Image::Scale;
    
    # Resize to 150 width and save to a file
    $logger->debug("Full Size File Name: $filename");
    my $img = Image::Scale->new($filename) || die "Invalid JPEG file";
    $img->resize_gd( { width => 249 } );
    $img->save_jpeg($TNfilename);
}
open IMAGE, $TNfilename or die "cannot open > $TNfilename: $!";
#assume is a jpeg...
my ($image, $buff);
while(read IMAGE, $buff, 1024) {
    $image .= $buff;
}
close IMAGE;
print "Content-type: image/jpeg\n\n";
print $image;
