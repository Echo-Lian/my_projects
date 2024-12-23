#!/bin/bash

# define two functions that can retrieve the basename and extension from a given path

get_basename() {
	# get the input path as an argument, store in a temperary file
	echo "$@" >> temp.txt
	# first separate the . as two arguments
	echo "$(awk -F "." '{print $1}' temp.txt)" >> temp2.txt
	awk -F "/" '{print $NF}' temp2.txt
	rm temp.txt temp2.txt
}