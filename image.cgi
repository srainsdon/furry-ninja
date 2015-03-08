#!/usr/bin/perl -w

use strict;
use CGI;
use diagnostics;
use CGI::Carp 'fatalsToBrowser';

my $BaseDir = "/var/www/images";

my $q = CGI->new();
my $UUID = $q->param('UUID');
my $filename = "$BaseDir/$UUID.jpg";

open IMAGE, $filename or die "cannot open > $filename: $!";
#assume is a jpeg...
my ($image, $buff);
while(read IMAGE, $buff, 1024) {
    $image .= $buff;
}
close IMAGE;
print "Content-type: image/jpeg\n\n";
print $image;
