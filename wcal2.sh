#!/bin/bash
show_year=false
while getopts "y" option; do
  case $option in
    y) show_year=true;;
  esac
done

today=($(date '+%Y %m %d')); Y=0; m=1; d=2                # establish today's date
[[ -z $1 ]] && ref=(${today[@]}) || ref=(${1//-/ })       # get input date
dNbA=$(date --date="$(date +%Y-%m-01)" +'%u')             # day-number of 1st day of reference month
today[m]=$((10#${today[m]})); ref[m]=$((10#${ref[m]}))    # remove leading zero (octal clash)
today[d]=$((10#${today[d]})); ref[d]=$((10#${ref[d]}))    # remove leading zero (octal clash)
nxtm=$(( ref[m]==12 ?1       :ref[m]+1 ))                 # month-number of next month
nxtY=$(( ref[m]==12 ?ref[Y]+1:ref[Y]   ))                 # year-number of next month
nxtA="$nxtY-$nxtm-1"                                      # date of 1st day of next month
refZ=$(date --date "$(date +$nxtA) yesterday" +%Y-%m-%d)  # date of last day of reference  month
days=$(date --date="$refZ" '+%d')                         # days in reference month

if $show_year; then
  for month in $(seq 1 12); do
    h1="$(date --date="${ref[Y]}-$month-01" '+%B %Y')" # header 1 
    h2="Mo Tu We Th Fr Sa Su"                                    # header 2 
    printf "    %$(((${#h2}-${#h1}-1)/2))s%s\n" " " "$h1"
    printf "    %s\n" "$h2"
    # print week rows   
    printf "%2d  " "$((10#$(date -d "$(date +${ref[Y]}-$month-01)" +'%V')))" # week-number (of year) with suppressed leading 0
    dNbA=$(date --date="$(date +${ref[Y]}-$month-01)" +'%u')             # day-number of 1st day of reference month
    printf "%$(((dNbA-1)*3))s"  # lead spaces (before start of month)
    dNbW=$dNbA  # day-number of week
    dNbM=1      # day-number of month
    for ((dNbM=1; dNbM<=$(cal $month ${ref[Y]} | awk 'NF {DAYS = $NF}; END {print DAYS}'); dNbM++))
    do
      if (( today[Y]==ref[Y] &&  
        today[m]==ref[m] &&
        today[m]==ref[m]&&
        today[d]==d
