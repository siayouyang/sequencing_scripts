#!/usr/bin/perl
#author:siayouyang
#use to remove 4 bases barcode
#usage: ./strip_barcode <raw.fq> <stripped.fq>

open IN, "$ARGV[0]";
open OU, ">$ARGV[1]";

while ($id=<IN>) {
        chomp($id);
        chomp($seq=<IN>);
        chomp($strand=<IN>);
        chomp($quality=<IN>);
        $strip_seq = substr($seq,4);
        $strip_quality = substr($quality,4);
        print OU "$id\n$strip_seq\n$strand\n$strip_quality\n";
}

close IN;
close OU;
