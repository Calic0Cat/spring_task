#!/usr/bin/perl
use strict;
use warnings;

my $count=0;
my $sum=0;
while(my $line=<>){
    chomp $line;
    $sum+=$line;
    $count++;
}

print $sum/$count,"\n" if($count!=0);