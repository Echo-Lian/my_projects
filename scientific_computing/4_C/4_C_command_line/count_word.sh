# within a file, serach every line of words whether it match the word.

for word in line
do
	grep -n -w "$word" $line
done
