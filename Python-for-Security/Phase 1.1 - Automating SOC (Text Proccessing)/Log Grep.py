import re
import os 
# i will check if the file using os

try:
    with open('incident_test_logs.txt', 'r') as file:
        content = file.read()
        # now, i will use re.findall to find all ips
        ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content)
        print(f"Found {len(ips)} IP addresses:") # len for counting the bumber of ips inside hte list.
        print (ips) 
except Exception as e:
    print(f"An error occurred: {e}")


