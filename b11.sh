echo "enter a number: "
read num
if [ $num -gt 0 ]
then 
	echo "number is positive.."
elif [ $num -lt 0 ]
then
	echo "number is negativ!!"
else
	echo "number is niether positive nor negative!!"
fi
