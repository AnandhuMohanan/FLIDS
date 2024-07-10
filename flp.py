import subprocess
import os
import time

# Define the paths to server.py and client.py
server_script_path = r"D:\Users\HP\Downloads\Test1\fl-ids-main (1)\fl-ids-main\server.py"
client_script_path = r"D:\Users\HP\Downloads\Test1\fl-ids-main (1)\fl-ids-main\client.py"
output_file_path = r"D:\Users\HP\Downloads\Test1\fl-ids-main (1)\fl-ids-main\output.txt"  # Full path to save the output of server.py

# Function to run a script in a new terminal
def run_script_in_terminal(script_path, output_file=None):
    if output_file:
        with open(output_file, "w") as f:
            subprocess.Popen(["start", "cmd", "/k", "python", script_path], stdout=f, stderr=f, shell=True)
    else:
        subprocess.Popen(["start", "cmd", "/k", "python", script_path], shell=True)

# Run server.py in a new terminal and save output to output.txt
print("Starting server...")
run_script_in_terminal(server_script_path, output_file=output_file_path)
time.sleep(2)  # Add a delay to ensure server starts before clients

# Run multiple instances of client.py in new terminals
num_clients = 3  # Change this to the number of client instances you want to run
print("Starting clients...")
for i in range(num_clients):
    print(f"Starting client {i+1}...")
    run_script_in_terminal(client_script_path)

print("All scripts started.")
