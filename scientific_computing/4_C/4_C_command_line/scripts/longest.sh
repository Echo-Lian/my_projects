# pipeline: input directory name; 
# list how many number of files;
# output the name of the files to a temporary txt file;
# word count to the temporary file;
# sort each temp file from every folder;
# return the directory name;
# delete the temp file;

for folder in "$@"
do
	ls $folder > $folder-n_files.txt
	wc $folder-n_files.txt >> rank_raw.txt
done

sort -n rank_raw.txt | tail -n 1

rm *files.txt
rm rank_raw.txt



