#!/bin/bash
echo "Starting scan "

for file in *.png; do
	zbarimg $file >> scanreport.txt
done
