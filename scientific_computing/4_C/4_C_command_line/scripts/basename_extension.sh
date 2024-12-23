#!/bin/bash

# Function to get the basename (before the first ".")
get_basename() {
    # Check if an argument is provided
    if [ -z "$1" ]; then
        echo ""
        return
    fi

    # Extract the filename from the path
    filename=$(basename "$1")

    # Check if it's a directory
    if [[ "$filename" == */ ]]; then
        echo ""
        return
    fi

    # If no ".", return the full filename; otherwise, split at the first "."
    if [[ "$filename" != *.* ]]; then
        echo "$filename"
    else
        echo "${filename%%.*}"
    fi
}

# Function to get the extension (after the last ".")
get_extension() {
    # Check if an argument is provided
    if [ -z "$1" ]; then
        echo ""
        return
    fi

    # Extract the filename from the path
    filename=$(basename "$1")

    # Check if it's a directory
    if [[ "$filename" == */ ]]; then
        echo ""
        return
    fi

    # If no ".", return a null string; otherwise, split at the last "."
    if [[ "$filename" != *.* ]]; then
        echo ""
    else
        echo "${filename##*.}"
    fi
}
