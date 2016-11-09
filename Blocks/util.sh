################################
# Calculates a given expression
#
# Dependencies:
# - bc
#
# @param {String} 1: The expression to calculate
# @return {Number}: The result of the expression
################################
calc() {
	echo "$1" | bc
}


################################
# Counts lines in text, accounting for empty values
#
# @param {String} 1: The input text
# @return {Number}: The number of lines
################################
numLines() {
	if [[ $1 == "" ]]; then
		echo 0
	else
		echo "$1" | wc -l
	fi
}
