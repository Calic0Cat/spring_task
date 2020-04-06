#!/bin/bash
echo -n >ERresult.txt
for i in `seq 1 100`
do
  perl 5-1.pl ERnetwork.txt >>ERresult.txt
done
cat ERresult.txt |perl average.pl