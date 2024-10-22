#!/bin/bash

# Ensure the script exits on any errors
set -e

# Check if the FlameGraph directory exists
if [ ! -d "./FlameGraph" ]; then
    echo "FlameGraph directory not found! Please clone from https://github.com/brendangregg/FlameGraph."
    exit 1
fi

# Set default duration (30 seconds if not specified)
DURATION=${1:-10}  # Default duration is 30 seconds if not provided

# Generate a timestamp-based filename for the output SVG
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_FILE="/mnt/flamegraph_${TIMESTAMP}.svg"

# Step 1: Run perf to record CPU usage system-wide for the specified duration
echo "Recording system-wide CPU usage with perf for $DURATION seconds..."
perf record -F 99 -a -g sleep $DURATION

# Step 2: Convert the perf output to a script format for FlameGraph input
echo "Generating perf script output..."
perf script > out.perf

# Step 3: Use stackcollapse-perf.pl from FlameGraph to convert the perf data into a collapsed format
echo "Converting perf data to collapsed stack format..."
./FlameGraph/stackcollapse-perf.pl out.perf > out.folded

# Step 4: Generate the flamegraph from the collapsed stack format
echo "Generating flamegraph..."
./FlameGraph/flamegraph.pl out.folded > "$OUTPUT_FILE"

# Clean up intermediate files
rm -f out.perf out.folded

echo "Flamegraph saved to $OUTPUT_FILE"
