lista=`ls $1` ;
var=0
varlocal=0
#printf "deletados $var de 80000 "
for i in $lista; do
	arquivo=`echo "$1$i"| sed 's/images/labels/g'|sed 's/jpg/txt/g'`
	#echo $arquivo
	if [ ! -f "$arquivo"  ]; then
		var=$((var+1))
		rm  "$1$i";
#		printf "\r"
#               printf "deletados $var de 80000 \|/"
	fi;
#	if [ $varlocal -eq 3 ];then
#		printf "\r"
#		varlocal=0
#		printf "deletados $var de 80000 "
#	fi
#	printf "."
	varlocal=$((varlocal+1))
        printf "deletados $var / $varlocal lidos \r"

done;

