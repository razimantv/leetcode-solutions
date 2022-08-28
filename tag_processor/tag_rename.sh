#!/bin/bash

while IFS= read -r line1 && IFS= read -r line2 <&3
do
  if [ "$line1" != "$line2" ]
  then
    echo "$line1 -> $line2"
    if [ -z ${subst+x} ]
    then
      subst="s!^$line1\$!$line2!g"
    else
      subst=$subst";s!^$line1\$!$line2!g"
    fi
  fi
done < tags.before 3< tags.after

sed -i "$subst" ./*/*/tags
