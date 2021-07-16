#!/bin/bash
#author:siayouyang
#filter out repetitive rRNA locus (chrXII:451275-469084)
#input format must be SAM
#usage ./removerRNAlocus.sh input.sam > output.sam

cat $1|awk '{if($3!~"chrXII" || $4<451275 && $4>469084 && $8<451275 && $8>469084 || $1~"^@")print}'
