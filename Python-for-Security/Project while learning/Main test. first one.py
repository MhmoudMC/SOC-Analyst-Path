#Main test subject haha.
ip_address = "192.168.1.1"
port_number = 443
threat_number = 65
print(f"Alert: This ip address {ip_address} is trying to connect with the database server on port {port_number}")
print(f"Alert: this ip {ip_address} is trying to connect with HR's laptop on port {port_number}")
print(22 % 5 )
print(10 * 60)


if threat_number > 80:
    print(f"Alert: this is a high threat number, please investigate immediately")
elif threat_number < 50:
    print(f"Alert: this an low threat number, let traffic pass")
else: 
    print(f"Alert: this is a medium threat number, please monitor the traffic closely")

