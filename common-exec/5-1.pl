#!/usr/bin/perl
use lib '/Users/SuzukiDaiki/perl/lib/perl5';
use Graph;
use Smart::Comments;
use List::Util;
use strict;
use warnings;


my $p = 0.05; #propagation probability
my $m=3; # number of seeds

my $graph_file=shift;

# read graph
my $g = Graph::Undirected->new;
open(IN,$graph_file) or die;
while(my $line=<IN>){
    chomp $line;
    my ($u,$v)=split(/ /,$line);
    $g->add_edge($u,$v);
}
close(IN);

my  @seeds=rand_m($g,$m);
my $active_node=spread_from($g,@seeds);

print $active_node,"\n";


# 次数の高い順にノードを m 個選ぶ
sub top_m{
    my $g=shift;
    my %degree;
    my $m=shift;
    my @array=sort {$g->degree($b)<=>$g->degree($a)} $g->vertices;
    my $count=0;
    my @nodes;
    foreach my $v (@array){
        push(@nodes,$v);
        $count++;
        if($count>=$m){
            last;
        }
    }
    return @nodes;
}

# ランダムに m ノード選ぶ

sub rand_m{
    my $g=shift;
    my $m=shift;
    my @array=$g->vertices;
    my @shuffled = List::Util::shuffle @array;
    my @nodes;
    for(1..$m){
        my $v =shift @shuffled;
        push(@nodes,$v);
    }
    return @nodes;
}

# 確率 p で independent-cascade spreading して、activate されたノードの
# リストを返す
sub spread_from {
    my ( $g, @seeds ) = @_;

    my %is_activated;
    foreach my $i (@seeds){
        $is_activated{$i}=1;
    }
    my %was_tried;
    my @to_try = grep { !$was_tried{$_} } keys %is_activated;
    while (@to_try) {
        for my $v (@to_try) {
            for my $u ( $g->neighbors($v) ) {
                next if $is_activated{$u};
                if ( rand() <= $p ) {
                    ### spread_from: "$v -> $u"
                    $is_activated{$u}++;
                }
            }
            $was_tried{$v}++;
        }
        @to_try = grep { !$was_tried{$_} } keys %is_activated;
    }
    ### spread_from: %is_activated
    return keys %is_activated;
}
