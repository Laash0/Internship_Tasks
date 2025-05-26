This will contain the description.

### Pre-requisites :

Downloaded 

1. nmap and
2. wireshark 

through the terminal.

---

## Scanning Process using NMAP

1. First of all we find out our subnet or IP address using the `ip a s` command.
2. Also we will need superuser access to run the nmap scans.
3. Then we use this subnet IP address to run nmap commands.
4. The most command scan is the TCP Syn Scan or Stealth Scan aka `sudo nmap -sS subnet_IP`
5. Another scan to run is the TCP Connect Scan aka `sudo nmap -sT subnet_IP`.
6. We can run the command to save output of these into file using the command `sudo nmap -oN output_file.txt` to save output in the file `output.txt`.
7. Since `-oN` always overwrites a file , therefore we will have to use different files to save output of both the commands.
8. We can now compile the results into one file , which in this case is `scan_results`.

In my case , the only open port was found out to be port **3306** which was being used by the service _`mysql`_ 

## Scanning Process using Wireshark

1. To start Wireshark , run the command `sudo wireshark`.
   1. It will now run with elevated privileges to access all interfaces of the system.
   2. Upon entering , we will see a list of interfaces to choose from.
2. We will select the correct interface , which in our case is `wlan0`.
3. After that we select the Capture option and select Start.
4. Now it will start capturing packets.
5. We can then end it whenever by clicking on red rectangle or the stop button.
6. After that , it is our discretion whether we want to save the file or not.

## Discussion

This table lists the most frequently used and commonly open ports observed in real-world networks — essential for scanning, enumeration, and securing systems.

| Port | Protocol | Service Name         | Description / Usage                                     |
|------|----------|----------------------|---------------------------------------------------------|
| 20   | TCP      | FTP (Data)           | File transfer (data connection)                         |
| 21   | TCP      | FTP (Control)        | File transfer (control/command)                         |
| 22   | TCP      | SSH                  | Secure remote login and command execution               |
| 23   | TCP      | Telnet               | Insecure remote login (mostly deprecated)               |
| 25   | TCP      | SMTP                 | Sending email                                           |
| 53   | UDP/TCP  | DNS                  | Resolving domain names                                 |
| 67   | UDP      | DHCP (Server)        | Assigning IP addresses                                 |
| 68   | UDP      | DHCP (Client)        | Receiving IP addresses                                 |
| 69   | UDP      | TFTP                 | Trivial file transfer protocol (insecure)               |
| 80   | TCP      | HTTP                 | Standard web traffic (unencrypted)                      |
| 110  | TCP      | POP3                 | Receiving email                                         |
| 123  | UDP      | NTP                  | Time synchronization                                   |
| 135  | TCP      | RPC                  | Microsoft Remote Procedure Call                         |
| 137  | UDP      | NetBIOS Name         | Windows file/printer sharing                            |
| 138  | UDP      | NetBIOS Datagram     | Windows legacy LAN communication                        |
| 139  | TCP      | NetBIOS Session      | Windows file/printer sharing                            |
| 143  | TCP      | IMAP                 | Email retrieval (alternative to POP3)                   |
| 161  | UDP      | SNMP                 | Network management/monitoring                           |
| 389  | TCP/UDP  | LDAP                 | Directory services (e.g., Active Directory)             |
| 443  | TCP      | HTTPS                | Secure web traffic                                      |
| 445  | TCP      | SMB                  | Windows file sharing (modern version)                   |
| 465  | TCP      | SMTPS                | Secure SMTP (email sending)                             |
| 514  | UDP      | Syslog               | Logging from network devices                            |
| 993  | TCP      | IMAPS                | Secure IMAP email                                       |
| 995  | TCP      | POP3S                | Secure POP3 email                                       |
| 1433 | TCP      | Microsoft SQL Server | Database connections                                    |
| 1723 | TCP      | PPTP                 | VPN tunneling (deprecated)                              |
| 3306 | TCP      | MySQL                | Database connections                                    |
| 3389 | TCP      | RDP                  | Remote Desktop Protocol (Windows)                       |
| 5060 | UDP/TCP  | SIP                  | VoIP signaling                                          |
| 5900 | TCP      | VNC                  | Remote desktop control                                  |
| 8080 | TCP      | HTTP-Alt             | Alternate web traffic port                              |

---

## Security Risks of Open Ports by Port Ranges

Open ports can expose services to the network, making them potential entry points for attackers. The type of risk depends on the port range and the service running.

### 1. Well-Known Ports (0–1023)

These ports are reserved for core system services and are often targeted first during reconnaissance.

#### Risks:

| Port | Service     | Risk Description |
|------|-------------|------------------|
| 22   | SSH         | Brute-force attacks, weak authentication, outdated versions |
| 80   | HTTP        | Unencrypted traffic, XSS, SQL injection, exposed admin panels |
| 443  | HTTPS       | SSL/TLS misconfigurations, certificate issues, exposed interfaces |
| 21   | FTP         | Plaintext credentials, anonymous login, file upload abuse |
| 25   | SMTP        | Spam relaying, spoofing, open relay exploitation |
| 53   | DNS         | Cache poisoning, DNS amplification attacks, info leakage |

### 2. Registered Ports (1024–49151)

Used by third-party or vendor-specific applications.

#### Risks:

| Port  | Service       | Risk Description |
|-------|---------------|------------------|
| 3306  | MySQL         | Unauthenticated access, SQL injection |
| 5432  | PostgreSQL    | Unprotected database exposure |
| 8080  | HTTP-Alt      | Test/staging servers, exposed APIs or admin consoles |
| 8443  | HTTPS-Alt     | Insecure HTTPS services, secondary control panels |
| 1723  | PPTP VPN      | Weak encryption, susceptible to VPN tunneling exploits |

### 3. Dynamic/Private Ports (49152–65535)

Used for temporary or custom service communication (e.g., peer-to-peer, malware C2, or backdoors).

#### Risks:

| Usage            | Risk Description |
|------------------|------------------|
| Backdoor traffic | Malware may bind services to high ports to avoid detection |
| P2P applications | Data leaks or C2 channels using unmonitored ports |
| Ephemeral ports  | Often left open due to firewall misconfigurations |

---

### General Security Risks of Open Ports

| Risk Type           | Description |
|---------------------|-------------|
| Firewall Bypass     | Exposes services beyond intended scope |
| Reconnaissance      | Enables attackers to discover OS, service versions, and entry points |
| Data Exfiltration   | Channels for leaking sensitive data |
| Exploits & RCE      | Vulnerable services may allow remote code execution |
| Malware Infection   | Services can be exploited to install malware |

### Best Practices

1. Close all unused ports at the firewall and host level.
2. Restrict access to sensitive ports using IP whitelisting.
3. Regularly scan the network for unexpected open ports.
4. Use VPNs or port-knocking for access to administrative services.
5. Keep all software and services patched and updated.


