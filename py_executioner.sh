#!/bin/bash

# Get time as a UNIX timestamp (seconds elapsed since Jan 1, 1970 0:00 UTC)
# In nanoseconds
T="$(($(date +%s%N)-T))"
M="$((T/1000000))"

# Do some work here
python pe1.py

echo "Time in milliseconds: ${M}"

#printf "Pretty format: %02d:%02d:%02d:%02d\n" "$((T/86400))" "$((T/3600%24))" "$((T/60%60))" "$((T%60))""
