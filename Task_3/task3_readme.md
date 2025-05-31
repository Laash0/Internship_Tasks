A **Vulnerability Scanner** is a security tool that automatically detects known weaknesses in systems, networks, or applications by scanning them and comparing results against a database of known vulnerabilities. It helps organizations **identify, assess, and prioritize security risks** to reduce exposure to cyberattacks.

OpenVAS (Open Vulnerability Assessment System) is an open-source vulnerability scanner used to assess the security of computer systems and networks by identifying known vulnerabilities. 

OpenVAS is part of the Greenbone Vulnerability Management (GVM) suite and serves as its core scanning engine.

| Feature       | OpenVAS                            | Nessus                       |
| ------------- | ---------------------------------- | ---------------------------- |
| Cost          | Free (open source)                 | Paid (Pro), Free (limited)   |
| Licensing     | Unlimited scans/IPs                | IP-limited (in free version) |
| Source Code   | Open and modifiable                | Closed-source                |
| Customization | High                               | Low to medium                |
| Usability     | Moderate (can be complex)          | Very user-friendly           |
| Support       | Community (free), Paid (Greenbone) | Professional (Tenable)       |

We will be picking OpenVAS today for its open-source nature.

## Installation and Setup

```
sudo apt install openvas
```

After that is done installing , we use another command to perform initial setup of GVM.


```
sudo gvm-setup
```

It performs the initial setup tasks necessary to make GVM and OpenVAS operational, including:

- Creates and configures GVM user(s)
- Initializes GVM services (like the scanner, manager, and web interface)
- Downloads vulnerability feeds (like NVTs, CERT, SCAP)
- Generates required certificates for secure communication
- Starts essential GVM components (e.g., gvmd, openvas, gsad)


The final step of this procedure is used to verify that Greenbone Vulnerability Management (GVM) — including its components like OpenVAS — is correctly installed and configured on your system.

```
sudo gvm-check-setup
```

---

## Starting Up and Scanning Procedure

```
sudo gvm-start
```

Note the web interface URL and login credentials provided.

Now to access the Web Interface , open a browser and visit:

```
https://127.0.0.1:9392
```

Login using the credentials created during setup.

---

### Set Up a Scan Target

- Go to Configuration > Targets
- Click “New Target”
- Name it `Localhost` for example.
- Set Host to 127.0.0.1 or your local IP_Address.
- Save

### Create and Launch a Scan Task

- Go to Scans > Tasks
- Click “New Task”
- Name: Full Scan Localhost
- Target: Select the target created earlier
- Scan Config: Choose Full and fast
- Click Create and Start Scan

### Wait for Scan to Complete

May take 30–60 minutes

Progress is visible under Scans > Tasks

---
---

## Report

**Scan Date:** May 29, 2025  
**Scan Type:** Full System Scan  
**Duration:** Approximately 6 minutes  
**Tool Used:** OpenVAS (GVM)

## Findings Overview

| Severity | Count |
|----------|-------|
| High     | 0     |
| Medium   | 1     |
| Low      | 0     |

---

### Identified Vulnerability

**Service:** PostgreSQL  
**Port:** 5432/tcp  
**Issue:** Weak SSL/TLS Cipher Suite  
**CVSS Score:** 5.9 (Medium)

**Details:**  
The service accepts the following weak cipher suite over TLSv1.2:  
`TLS_RSA_WITH_SEED_CBC_SHA`

**Impact:**  
Use of weak cipher suites compromises the security of encrypted communications and may allow attackers to intercept or decrypt sensitive information.

---

### Recommended Mitigation

- Reconfigure the affected service to disable the use of weak cipher suites.
- Only allow strong, modern cipher suites such as AES-GCM with forward secrecy.
- Ensure TLS versions below 1.2 are disabled.

**Useful References:**
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org)
- [CVE-2013-2566](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-2566)
- [CVE-2015-2808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2808)
- [CVE-2015-4000](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4000)
