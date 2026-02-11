# This is an answer for a request .
print("Analyzing attacker frequency...")
print("Processing raw logs...")
print("Updating attempt frequency...")
print("Final attempt frequency:")
raw_logs = ["192.1.1.1",
            "192.1.1.2",
            "192.1.1.3",
            "192.1.1.4",
            "192.1.1.5",
            "192.1.1.6",
            "192.1.1.7",
            "192.1.1.8",
            "192.1.1.9",
            
            "192.1.1.8",
            "192.1.1.9",
            "192.1.1.99",
            "192.1.1.100"
            ]
attempt_frequency = {"192.1.1.1" : 5,
                     "192.1.1.2" : 3,
                     "192.1.1.3" : 7,
                     "192.1.1.4" : 2,
                     "192.1.1.5" : 6,
                     "192.1.1.6" : 4,
                     "192.1.1.7" : 8,
                     "192.1.1.8" : 3,
                     "192.1.1.9" : 5,
                     "192.1.1.10" : 7,
                     
                     }

for ip in raw_logs:
    if ip in attempt_frequency:
        attempt_frequency[ip] += 1
    else:
        attempt_frequency[ip] = 1

print(attempt_frequency)