# A list of raw logs from the server
raw_logs = [
    "   Failed Login from 192.168.1.50   ",
    "Successful Login from 10.0.0.5",
    "   Failed Login from 172.16.0.25      ",
    "Successful Login from 192.168.1.100",
    "Failed Login from 1.1.1.1"
]

# Our SOC Blacklist
blacklist = ["1.1.1.1", "192.168.1.50"]

print("--- Log Analysis Started ---")

# Step 1: Loop through every log [cite: 60]
for log in raw_logs:
    # Here i wanna clean the log by removing spaces
    clean_log = log.strip()
    
    # here if it said failed login, i wanna print it.
    if "Failed" in clean_log:
        # split the sentence into equalevents inside the list {words}
        words = clean_log.split()
        
        # Taking the ip, it should be the 4th word each time.
        ip = words[3]
        
        # if the ip is in our black list, we will print an alert, otherwise it well just say he failed
        if ip in blacklist:
            print(f"🚨 ALERT: {ip} is a known attacker!")
        else:
            print(f"Notice: Failed login from {ip} (Not blacklisted).")

print("--- Scan Complete ---")