#!/bin/sh
sed -i \
         -e 's/rgb(0%,0%,0%)/#eeeeee/g' \
         -e 's/rgb(100%,100%,100%)/#555555/g' \
    -e 's/rgb(50%,0%,0%)/#444444/g' \
     -e 's/rgb(0%,50%,0%)/#02c0fa/g' \
 -e 's/rgb(0%,50.196078%,0%)/#02c0fa/g' \
     -e 's/rgb(50%,0%,50%)/#cccccc/g' \
 -e 's/rgb(50.196078%,0%,50.196078%)/#cccccc/g' \
     -e 's/rgb(0%,0%,50%)/#1a1a1a/g' \
	*.svg