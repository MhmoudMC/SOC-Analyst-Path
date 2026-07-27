MAHMOUD ELBADREY
SOC Analyst | Detection Engineering | Security Engineering Foundations
Libya | mhmoud.elbadrey@gmail.com | github.com/MhmoudMC | Open to SOC L1/L2 & Security Engineering Roles

---

## SUMMARY

SOC Analyst with hands-on incident investigation, Splunk detection engineering, and Python automation. Completed Phase 0-1 SOC fundamentals (60+ lessons) and TryHackMe Blue Team Path (full completion). Built full breach analysis from brute-force to 2.5GB exfiltration, including timeline reconstruction, IOC extraction, and containment recommendations. Comfortable with log correlation, alert tuning, malware handling, and system recovery. Ready for SOC L1/L2 or security engineering roles. Currently enrolled in AI Track university (flexible with schedule for remote work).

---

## CORE SKILLS

**SIEM & Detection:**
- Splunk: SPL queries, dashboards, real-time alerting, detection rule engineering
- Detection Engineering: brute-force detection, privilege escalation patterns, data exfiltration baselining, alert tuning & false positive reduction
- Anomaly Monitoring: frequency analysis, statistical baselines, outlier identification

**Incident Investigation & Response:**
- Log triage and correlation (multi-source log analysis)
- IOC extraction and documentation
- Attack timeline reconstruction (chronological analysis)
- Containment recommendations and escalation logic
- Incident reporting and formal documentation

**Programming & Automation:**
- Python: log parsing, regex, file extraction, data structure manipulation, simple statistical detection
- Security Tooling: custom scripts for log analysis, threat scoring, IP validation
- Scripting: bash basics for system troubleshooting

**Systems & Networking:**
- TCP/IP fundamentals
- Firewall and IDS log analysis
- Windows Event Logs (Security, System, Application)
- Linux syslog, auth.log, system logs
- Process analysis and service troubleshooting

**Malware & Incident Recovery:**
- Safe sample handling and chain of custody
- Hash verification (MD5/SHA256)
- Static analysis preparation
- Physical system troubleshooting and recovery
- Ransomware response basics

---

## CERTIFICATIONS & TRAINING

**TryHackMe Blue Team Path** — Complete (100% path completion)
- Covered: Windows fundamentals, Linux fundamentals, log analysis, threat detection, incident response workflows
- Proof: TryHackMe profile with all modules completed

**SOC Fundamentals (Self-Directed)** — Phase 0-1 Complete
- Phase 0: Networking, logs, alerts, incident response concepts (36 lessons)
- Phase 1: SIEM operations, detection engineering, incident workflows (25+ lessons)
- Proof: GitHub documentation + structured learning path

**Python for Security** — Phase 1.0-1.1 Complete
- Fundamentals: variables, loops, dictionaries, lists, control flow
- SOC Automation: file I/O, regex, log parsing, data structures
- Proof: Working security tools on GitHub

---

## SELECTED PROJECTS

### Full Breach Investigation — Splunk & Log Correlation

**Objective:** Analyze simulated breach from initial access through data exfiltration

**Methodology:**
- Tracked external attacker (IP: 185.220.101.4) through multi-stage attack chain
- Correlated SSH auth logs, firewall connection logs, database query logs, and Windows process events
- Built chronological attack timeline spanning 36 hours (Oct 10 22:15 - Oct 12 08:30)

**Key Findings:**
- Identified 12+ Indicators of Compromise (IOCs): malicious IPs, suspicious domains, file hashes
- Detected lateral movement from compromised user account (jsmith) to internal server (10.0.0.100)
- Traced data exfiltration: 2.5GB stolen across 3 separate connections to external IP (45.134.26.78)
- Identified persistence mechanism: malware installation (updater.exe), Windows Defender disabled, registry modifications

**Recommendations:**
- Account lockout and credential reset for compromised account
- Network isolation for affected workstations and servers
- Detection rule hardening for beaconing and large data transfers
- Escalation to L2 analyst team for forensic deep-dive

**Outcome:** Complete incident report with attack chain, timeline, and containment steps

**Proof:** [github.com/MhmoudMC/SOC-Analyst-Path](https://github.com/MhmoudMC/SOC-Analyst-Path)

---

### Detection Rule Engineering — Splunk SPL

**Objective:** Implement detection logic for common attack patterns

**Rules Implemented:**
1. **Brute Force Detection:** Flag IPs with >5 failed SSH/RDP logins in 10-minute window
2. **Privilege Escalation:** Alert on unexpected sudo commands or schtasks execution
3. **Data Exfiltration:** Detect outbound connections with >500MB data transfer in 1 hour
4. **Suspicious Process Execution:** Flag executables launched from temp directories or downloads folder
5. **Lateral Movement:** Identify failed logon attempts to multiple internal systems from single source

**Process:**
- Wrote SPL queries with proper aggregation (stats, groupby, timechart)
- Tested with synthetic events to validate detection logic
- Tuned thresholds to reduce false positives while maintaining sensitivity
- Documented testing methodology and alert triggers

**Outcome:** Reusable detection rules ready for production SIEM deployment

**Proof:** [github.com/MhmoudMC/SOC-Analyst-Path](https://github.com/MhmoudMC/SOC-Analyst-Path)

---

### Python Security Tooling — Automation & Log Parsing

**Tools Built:**

1. **Intruder Finder**
   - Purpose: Match IP addresses against known attacker blacklist
   - Functionality: Parse logs, extract IPs, cross-reference blacklist, generate alerts
   - Use case: Quick identification of known malicious sources

2. **Log IP Extractor**
   - Purpose: Extract IP addresses from multi-format log files (mixed formats, various delimiters)
   - Functionality: Regex-based extraction, validation, deduplication
   - Use case: Automated IOC collection from diverse log sources

3. **Failed Login Monitor**
   - Purpose: Detect authentication attacks and suspicious login patterns
   - Functionality: Parse auth logs, identify failed attempts, count frequency, escalate
   - Use case: Real-time brute-force detection

**Technical Details:**
- Implemented proper error handling (try/except)
- Used regex for pattern matching across log formats
- Applied data structures (lists, dicts) for efficient lookups
- Documented code with clear comments

**Proof:** [github.com/MhmoudMC/SOC-Analyst-Path/Python-for-Security](https://github.com/MhmoudMC/SOC-Analyst-Path)

---

### Incident Response: Malware Recovery & Analysis

**Scenario:** Suspected ransomware-infected laptop

**Actions Taken:**

**Physical Recovery:**
- Safely isolated laptop from network (prevent lateral movement)
- Disconnected non-essential peripherals (reduce attack surface)
- Upgraded RAM from 2GB to 4GB (improved analysis capability)
- Documented all actions (chain of custody)

**Malware Handling:**
- Extracted suspicious sample safely (no execution on production system)
- Moved sample to isolated Linux environment for static analysis
- Avoided dynamic execution (no sandbox detonation without approval)
- Verified sample integrity using MD5/SHA256 hash checking

**Outcome:**
- System revived and safe for forensic analysis
- Malware sample preserved for threat analysis
- Demonstrated understanding of incident response protocols and safe malware handling

**Proof:** Real project completion, documented in GitHub

---

### Splunk SOC Dashboard — Real-Time Monitoring

**Objective:** Build analyst-focused dashboard for alert surfacing

**Dashboard Components:**
- **Failed Login Heatmap:** Frequency of failed logins by hour and source IP
- **Top Attack Sources:** IP addresses with most connection attempts (real-time ranking)
- **Suspicious Executable Activity:** Processes launched from unusual directories
- **Data Transfer Anomalies:** Outbound connections with unusually large data transfers

**Technical Implementation:**
- Built with Splunk SPL queries (stats, timechart, eval for calculations)
- 30-second refresh interval for real-time alerting capability
- Color-coded severity (green/yellow/red) for quick analyst triage
- Drill-down capability to investigate individual events

**Use Case:** Frontline SOC analyst tool for rapid threat identification and initial triage

**Proof:** Dashboard published in Splunk environment

---

## GITHUB PORTFOLIO

**Repository:** github.com/MhmoudMC/SOC-Analyst-Path

**Activity:**
- 137+ total contributions
- 60+ SOC lessons documented
- Full investigation case studies with analysis
- Working security tools and scripts
- Consistent commit history showing sustained learning

**Structure:**
- Phase 0: Networking fundamentals (documented learning path)
- Phase 1: SIEM operations and incident response (structured lessons + projects)
- Python-for-Security: Tool implementations with documentation
- Investigations: Complete incident writeups with methodology
- Images & Documentation: SIEM dashboard screenshots, incident timelines

---

## EDUCATION & TRAINING

**AI Route Training Program** — AI Track, Benghazi, Libya | Currently Enrolled
- AI specialization pathway
- Currently in 2nd semester
- Flexible schedule for professional opportunities
- Strong academic standing

**Self-Directed SOC Training** — Complete
- Phase 0 (36 lessons): Networking, logs, incident response fundamentals
- Phase 1 (25+ lessons): SIEM operations, detection engineering, incident workflows
- Structured learning with hands-on projects
- Proof: GitHub documentation and completed projects

**TryHackMe Blue Team Path** — Complete
- Comprehensive blue team training (100% path completion)
- Covered: Windows/Linux fundamentals, log analysis, threat detection, incident response
- Hands-on labs with real-world scenarios
- Proof: TryHackMe profile badges

**Python for Security** — Phase 1.0-1.1 Complete
- Python fundamentals (variables, loops, data structures, control flow)
- SOC automation (file I/O, regex, log parsing, data structures)
- Applied learning with security tools
- In progress: Phase 1.2-1.3 (NumPy, Pandas, statistical detection)

---

## TECHNICAL EXPERIENCE SUMMARY

**SIEM Operations:**
- Splunk: Data ingestion, parsing, querying (SPL), dashboards, alerting
- Detection Engineering: Threshold-based rules, anomaly detection, alert tuning
- Log Analysis: Multi-source correlation, timeline reconstruction, IOC extraction

**Incident Response:**
- Initial triage and severity assessment
- Log correlation and root cause analysis
- Attack timeline construction
- Containment and escalation recommendations
- Formal incident reporting

**Python & Automation:**
- Log parsing and regex pattern matching
- File I/O and data manipulation
- Custom security tools development
- Basic statistical analysis

**Systems & Networking:**
- Windows Event Log analysis
- Linux syslog and auth.log analysis
- Firewall and IDS log interpretation
- Process and service troubleshooting

**Malware & Recovery:**
- Safe sample handling and analysis
- Chain of custody documentation
- Hash verification
- System recovery and forensics preparation

---

## AVAILABILITY & WORK STYLE

**Availability:**
- Available for remote start immediately
- Currently enrolled in university (flexible with remote schedule)
- Open to relocation after project completion
- Timezone advantage: MENA region (works well with EU companies)

**Work Approach:**
- Disciplined daily practice (consistent GitHub activity proves this)
- Strong documentation (technical writing, clear communication)
- Remote-capable (proven through self-directed learning)
- Self-directed learner (independent problem-solving)
- Detail-oriented (incident investigation requires precision)

**Languages:**
- Arabic (native)
- English (professional working proficiency)

---

## WHAT'S NEXT

**In Progress:**
- Python Phase 1.2-1.3: NumPy, Pandas, statistical detection
- Adaptive SIEM Project: Per-user behavioral baselining with Z-score anomaly detection
- Continued TryHackMe labs and Splunk querying
- Real-world incident response scenarios

**Seeking:**
- SOC L1 or L2 role (remote or relocate)
- Security engineering internship
- Detection engineering opportunity
- Incident response analyst position

**Open to:** Remote roles, relocation to EU/MENA region, contract/freelance opportunities

---

## CONTACT & LINKS

- **Email:** mhmoud.elbadrey@gmail.com
- **GitHub:** github.com/MhmoudMC
- **Location:** Libya (Remote-capable)
- **Languages:** Arabic (native), English (professional)

---

*Resume updated: January 2025 | Last Updated: [Current Date]*
