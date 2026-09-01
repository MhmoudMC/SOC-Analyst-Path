import re, os, numpy as np, scipy.stats as stats
print("Current Directory: ", os.getcwd())
print("files found: ", os.listdir('.'))
yes = "incident_test_logs.txt"
log_file = input("Write the name of one of the logs you are looking for in the current working directory: ")
if log_file == "yes" :
    log_file = yes

number_pattern = r'\d{1,2}:\d{1,2}'
bits_pattern = r'\d{1,3}'
time_count = {}
bits = []
try :  
    with open("Incident_test_logs.csv", "r") as file :
        print ("Did it work ?")
        log = file.readlines() 
        for event in log :
            clean_event = event.strip()
            useable_time = clean_event.split(",")
            if re.findall(number_pattern, useable_time[0]) :
                print("Time found: ", useable_time[0])
                print("Bits found: ", useable_time[1])
                bits.append(int(useable_time[1]))
        print("Bits found: ", bits)
        median_bits = np.median(bits)
        mean_bits = np.mean(bits)
        std_dev_bits = np.std(bits)
        print(f"Median bits: {median_bits}, Mean bits: {mean_bits}, Standard Deviation bits: {std_dev_bits}")
        for bit in bits :
            if bit > median_bits + 2 * std_dev_bits :
                print(f"Anomaly detected: {bit} bits exceeds the threshold of {median_bits + 2 * std_dev_bits}")



except FileNotFoundError:
    print("File not found. Please Check the file path and name.")
