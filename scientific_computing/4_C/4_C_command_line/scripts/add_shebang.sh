#!/bin/bash

# Usage:
# check if the file/files provided;
# iterate over all provided arguments;
# check if the file is empty or not;
# check each file has shebang for the first line(head -n 1 matches the shebang or not)
# if yes, do nothing;
# if no, insert a shebang; (sed -i $'1i\\\n#!/bin/bash\n' $file)

# define shebang
shebang="#!/bin/bash"

for file in "$@"; do
	# check if the file exists
	if [ ! -f "$file" ]; then
		echo "$file does not exist!"
		continue
	fi
	
	# check if the file is empty or not
	# if not empty, insert shebang
	if [ -s "$file" ]; then
		# extract the first line
		first_line=$(head -n 1 "$file")
		
		# check if the first line matches the shebang
		# if not, insert a shebang	
		if [ "$first_line" != "$shebang" ];then
			sed -i '' $'1i\\\n#!/bin/bash\n' "$file"
		else
			echo "shebang already existed in $file!"
		fi

	# empty, insert the shebang directly
	else
		echo "#!/bin/bash" >> $file
	fi
done
