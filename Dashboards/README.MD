# First Splunk Dashboard

![dashboard](https://github.com/MhmoudMC/SOC-Analyst-Path/blob/main/Dashboards/The%20Main%20Dashboard.pdf)

**Purpose:** Monitor failed login attempts in real-time

**Key Querys:**
- Failed Logins Attempts [source="incident_test_logs.txt" host="Mhmoud" sourcetype="2023" "Failed"]
- High Data Transforming Panel [source="incident_test_logs.txt" host="Mhmoud" sourcetype="2023" 2.5gb]
- .exe Activities [source="incident_test_logs.txt" host="Mhmoud" sourcetype="2023" 2.5gb]
- High IP Frequency {refresh every 30s} [source="incident_test_logs.txt" host="Mhmoud" sourcetype="2023" | rex field=_raw max_match=0 "(?<all_ips>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" | mvexpand all_ips | stats count by all_ips | sort - count]


