#!/usr/bin/env bash

#port 12345. output goes to output.txt
while true; do
  sudo nc -l -p 12345 >> output.txt
done