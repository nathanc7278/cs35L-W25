#!/bin/bash

git log --pretty=format:"%cd" $1 | awk '{print $NF}' | sort -n | uniq -c | awk '{print $2, $1}'