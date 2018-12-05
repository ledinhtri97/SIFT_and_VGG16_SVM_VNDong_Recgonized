for fn in $(ls *.jpg); do 
    name=${fn##*/}
    base=${name%.jpg*}
    convert  -resize 10% $fn $base.jpg
done