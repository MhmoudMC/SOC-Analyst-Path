import re 
import os 
import numpy as np
from scipy import stats 

yes = "incident_test_logs.txt"
print("files found: ", os.listdir('.'))
log_file = input("Write the name of one of the logs you are looking for in the current working directory: ") 

if log_file == "yes":
    log_file = yes

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

try :
    with open(log_file, "r") as file: 

        log = file.readlines() # this made log a list of strings

        print("Current working directory:", os.getcwd())

        total_failed_logins = 0
        
        ip_count = {}
        failed_ip_count = {}

        for event in log :
            cleaned_event = event.strip()
            for ip in re.findall(ip_pattern, cleaned_event) :
                if ip in ip_count:
                    ip_count[ip] += 1
                else:
                    ip_count[ip] = 1
            for ip in re.findall(ip_pattern, cleaned_event) :
                if "failed" in cleaned_event.lower() or "error" in cleaned_event.lower() :
                    if ip in failed_ip_count:
                        failed_ip_count[ip] += 1
                    else:
                        failed_ip_count[ip] = 1
            if "failed" in cleaned_event.lower() or "error" in cleaned_event.lower() :
                total_failed_logins += 1
    
    print(f"IP-count for events is {ip_count}")
    print(f"IP-count for failed events is {failed_ip_count}")
    print(f"Total failed logins: {total_failed_logins}")

    counts = list(ip_count.values())
    mean = np.mean(counts)
    std_dev = np.std(counts)
    threshold = mean + 0.75 * std_dev

    for ip, count in ip_count.items() : 
        if count > threshold :
            print(f"Anomaly detected: {ip} has {count} events, which exceeds the threshold of {threshold}")

    chance = stats.binom.pmf(total_failed_logins, len(log), 0.05)
    print(f"Probability of failed logins being normal: {chance}")
except FileNotFoundError:
    print("File not found. Please check the file path and name.")
