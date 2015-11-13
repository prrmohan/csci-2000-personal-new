#!/bin/bash
# Priya Mohan - 100503515

# $1 is the leading number of lines to be removed
# $2 is the trailing number of lines to be removed
# $3 is the filename to read from

# prints result to screen (or to file if > filename is used in cmd)

tail -n +$1 $3 | head -n -$2 