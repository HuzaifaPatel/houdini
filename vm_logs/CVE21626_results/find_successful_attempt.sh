#!/bin/bash

SEARCH_STRING="The Quick Brown Fox"
# SEARCH_STRING="Error building Docker image: toomanyrequests: You have reached your unauthenticated pull rate limit."

echo "🔍 Searching for matching lines in all .log files..."

find . -type f -name "*.log" | while read -r file; do
    # Use grep with -F (fixed string) and -H (print filename) to show matching files
    grep -F "$SEARCH_STRING" "$file" && echo "✅ Found in: $file"
done

echo "✅ Done."
