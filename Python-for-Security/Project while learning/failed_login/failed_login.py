

with open("server_logs.txt", "r") as file:
    for line in file:
        line = line.split() # here i split the 
        if line[7] == "Failed":
            with open("alerts.txt", "a") as alert:
                alert.write(f"Alert: Failed login attempt at {line[0]} {line[1]}\n")
        else:
            with open("alerts.txt", "a") as alert:
                alert.write(f"Successful login at {line[0]} {line[1]}\n")
                