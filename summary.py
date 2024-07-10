import streamlit as st
import subprocess
import os

# Check if the server process is running
server_process = None
output_lines = []

# Function to capture server output
def capture_server_output():
    global output_lines
    while True:
        line = server_process.stdout.readline().strip()
        if line == '[SUMMARY]':
            output_lines.append(line)
            break
        output_lines.append(line)

    # Continue reading and appending lines until the end of output
    while True:
        line = server_process.stdout.readline().strip()
        output_lines.append(line)
        if not line:
            break

    # Write output to a file
    with open('output.txt', 'w') as f:
        f.write('\n'.join(output_lines))

    # Print any errors
    if server_process.returncode != 0:
        print("Error occurred:", server_process.stderr)
    else:
        print("Output saved to output.txt")

# Execute server process first
# Example command: python server.py
server_command = ['python', 'server.py']
server_process = subprocess.Popen(server_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the server process to complete
server_process.wait()

# Capture server output if process was running
if server_process.poll() is None:
    capture_server_output()
else:
    print("Server process has terminated before capturing output.")
