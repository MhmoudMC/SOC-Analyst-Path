blacklist = ["192.168.1.100", "10.0.0.50", "172.16.0.5", "192.168.1.100"] # the developer have alerady some bad IPs known, maybe they got it from a papular website  that gives bad ips,
blacklist.append("45.33.22.11") # After blocking the Brute-Force attempt, the soc analyst (Me) tould the developer to add that ip.
print(blacklist[2]) # after analyst investigating the Logs, it turned out that IP is 40% incent. still under investigation.
print(f"The black list contains {len(blacklist)} IP addresses.") # The developer asked about the number of IPs in the blacklist, 
