#!/bin/bash

for i in */*/
do
  cat ./*/*/tags | sort | uniq > tags
  cd "$i" || exit
  if [ ! -f tags ]
  then
    vi -p ./Solution.* tags ../../tags
  fi
  cd ../..
done

