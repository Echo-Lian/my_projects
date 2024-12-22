#!/bin/bash

# check if at least one file is provided
if [[ $# -eq 0 ]]; then
	echo 'Usage: $0 file1 file2 file3 ...'
	exit 1
fi

# iterate over all provided arguments
for file in "$@"; do
	# check if the file exists
	if [[ -f '$file' ]]; then
		# check if the file already starts with a shebang
		first_line=$(head -n 1 '$file')
		if [[ '$first_line' != '#!'* ]]; then
			# add the shebang line at the beginning of the file
			sed -i '' $'1i\\\n#!/bin/bash\n' "$file"
			echo 'Add shebang to $file.'
		else
			echo 'Shebang already present in $file'
		fi
	else
		echo 'File $file does not exist, skipping'
	fi
done
