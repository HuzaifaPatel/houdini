import subprocess

# Run the 'ps aux' command and capture the output
ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)

# Use grep to filter the output for "server.py"
grep = subprocess.Popen(['grep', ' python3 server.py'], stdin=ps.stdout, stdout=subprocess.PIPE)

# Close the output from 'ps' so grep can finish
ps.stdout.close()

# Get the output from grep
output, _ = grep.communicate()

# Decode and print the output
print(output.decode('utf-8'))