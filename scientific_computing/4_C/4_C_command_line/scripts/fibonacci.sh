#!/bin/bash

# Fibonacci function
fibonacci() {
  # Check if input is provided
  if [ -z "$1" ]; then
    echo "Error: No input provided"
    return 1
  fi

  # Check if input is a valid integer
  if ! [[ "$1" =~ ^-?[0-9]+$ ]]; then
    echo "Error: Input must be an integer"
    return 1
  fi

  # Get the input number
  local n=$1

  # Handle negative numbers
  if [ "$n" -lt 0 ]; then
    echo "Error: Negative numbers are not allowed"
    return 1
  fi

  # Handle base cases
  if [ "$n" -eq 0 ]; then
    echo 0
    return 0
  elif [ "$n" -eq 1 ]; then
    echo 1
    return 0
  fi

  # Compute Fibonacci iteratively
  local a=0
  local b=1
  local temp

  for (( i=2; i<=n; i++ )); do
    temp=$((a + b))
    a=$b
    b=$temp
  done

  echo "$b"
  return 0
}
