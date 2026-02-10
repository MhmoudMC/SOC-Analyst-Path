blacklist = ["1.1.1.1", "8.8.8.8", "192.168.5.50"]
recent_connections = ["192.168.1.10", "1.1.1.1", "10.0.0.5", "192.168.5.50", "172.16.0.1"]

print("--- GATEKEEPER SYSTEM STARTING ---")

for ip in recent_connections:
    if ip in blacklist:
        print(f"[!] ALERT: Blocked connection from {ip}")
    else:
        print(f"[+] Safe: {ip} allowed.")

print("--- SCAN FINISHED ---")

# --- THE WHILE LOOP ---
while True:
    user_input = input("Enter an IP to check, or exit to quit: ")
    
    if user_input == "exit":
        break
    elif user_input in blacklist:
        print(f"WARNING: The IP {user_input} is blacklisted!")
    else:         
        print(f"The IP {user_input} is safe.")