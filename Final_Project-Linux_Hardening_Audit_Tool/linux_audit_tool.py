#!/usr/bin/env python3

import os
import subprocess
import shutil
from datetime import datetime

report = []
score = 0
max_score = 0
recommendations = []

# General Audit Section #

def check_firewall():
    global score, max_score
    max_score += 1
    try:
        ufw_path = shutil.which("ufw")
        firewall_cmd_path = shutil.which("firewall-cmd")

        if ufw_path:
            status = subprocess.getoutput("sudo ufw status")
            if "inactive" in status.lower():
                report.append("❌ UFW firewall is inactive.")
                recommendations.append("Enable UFW firewall using: sudo ufw enable")
            else:
                report.append("✅ UFW firewall is active.\n" + status)
                score += 1
        elif firewall_cmd_path:
            status = subprocess.getoutput("sudo firewall-cmd --state")
            if "running" in status.lower():
                report.append("✅ firewalld is active.")
                score += 1
            else:
                report.append("❌ firewalld is not active.")
                recommendations.append("Start firewalld using: sudo systemctl start firewalld")
        else:
            report.append("⚠️ No known firewall manager (ufw/firewalld) found.")
            recommendations.append("Install and enable a firewall (ufw or firewalld).")
    except Exception as e:
        report.append(f"⚠️ Firewall check failed: {e}")

def check_auditd():
    global score, max_score
    max_score += 1
    try:
        status = subprocess.getoutput('systemctl is-active auditd')
        if status.strip() == 'active':
            report.append("✅ auditd is active.")
            score += 1
        else:
            report.append("❌ auditd is not active.")
            recommendations.append("Enable auditing: sudo systemctl enable --now auditd")
    except Exception as e:
        report.append(f"⚠️ Auditd check failed: {e}")

def check_ssh():
    global score, max_score
    max_score += 2
    ssh_file = "/etc/ssh/sshd_config"
    if not os.path.exists(ssh_file):
        report.append("⚠️ SSH config file not found.")
        return

    findings = []
    expected_settings = {
        "PermitRootLogin": "no",
        "PasswordAuthentication": "no"
    }

    with open(ssh_file, "r") as f:
        config_lines = f.readlines()

    for key, expected_value in expected_settings.items():
        found = False
        for line in config_lines:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            if line.lower().startswith(key.lower()):
                found = True
                parts = line.split()
                if len(parts) >= 2 and parts[1].lower() == expected_value.lower():
                    findings.append(f"✅ {key} is properly set.")
                    score += 1
                else:
                    findings.append(f"❌ {key} is not set to '{expected_value}' (found: {line})")
                    recommendations.append(f"Set {key} to {expected_value} in {ssh_file}")
                break
        if not found:
            findings.append(f"⚠️ {key} setting not found in SSH config.")
            recommendations.append(f"Add {key} {expected_value} to {ssh_file}")

    report.append("🔐 SSH Configuration:\n" + "\n".join(findings))

def check_permissions():
    global score, max_score
    files = [("/etc/passwd", "644"), ("/etc/shadow", "640")]
    findings = []

    for file, expected_mode in files:
        max_score += 1
        try:
            stat_info = os.stat(file)
            mode = oct(stat_info.st_mode)[-3:]
            if file == "/etc/passwd" and mode != expected_mode:
                findings.append(f"❌ {file} permissions should be {expected_mode} but are {mode}")
                recommendations.append(f"Fix permissions with: sudo chmod 644 {file}")
            elif file == "/etc/shadow" and mode not in ["640", "400", "000"]:
                findings.append(f"❌ {file} permissions should be 640, 400, or stricter but are {mode}")
                recommendations.append(f"Fix permissions with: sudo chmod 640 {file}")
            else:
                findings.append(f"✅ {file} permissions are {mode} (OK)")
                score += 1
        except Exception as e:
            findings.append(f"⚠️ Could not check {file}: {e}")

    report.append("🔒 File Permissions:\n" + "\n".join(findings))

def check_rootkits():
    global score, max_score
    max_score += 1
    chkrootkit = shutil.which("chkrootkit")
    if not chkrootkit:
        report.append("⚠️ chkrootkit not installed. Skipping rootkit scan.")
        recommendations.append("Install chkrootkit with: sudo apt/dnf/pacman install chkrootkit")
        return

    try:
        output = subprocess.getoutput("sudo chkrootkit")
        if "INFECTED" in output:
            report.append("❌ Rootkit indicators found!\n" + output)
        else:
            report.append("✅ No rootkits found.")
            score += 1
    except Exception as e:
        report.append(f"⚠️ Rootkit check failed: {e}")

def check_updates():
    global score, max_score
    max_score += 1
    try:
      
        # For Debian/Ubuntu
        if shutil.which("apt"):
            output = subprocess.getoutput("apt list --upgradable 2>/dev/null | grep -v Listing")
            if output.strip():
                report.append("❌ System has pending updates.")
                recommendations.append("Update system packages: sudo apt update && sudo apt upgrade")
            else:
                report.append("✅ System is up to date.")
                score += 1
              
        # For RHEL/CentOS/Fedora
        elif shutil.which("dnf"):
            output = subprocess.getoutput("dnf check-update")
            if output.strip():
                report.append("❌ System has pending updates.")
                recommendations.append("Update system packages: sudo dnf upgrade")
            else:
                report.append("✅ System is up to date.")
                score += 1
              
        # For Arch Linux
        elif shutil.which("pacman"):
            # Try checkupdates first, fallback to pacman -Qu
            if shutil.which("checkupdates"):
                output = subprocess.getoutput("checkupdates")
            else:
                output = subprocess.getoutput("pacman -Qu")
            if output.strip():
                report.append("❌ System has pending updates.")
                recommendations.append("Update system packages: sudo pacman -Syu")
            else:
                report.append("✅ System is up to date.")
                score += 1
        else:
            report.append("⚠️ Could not determine package manager for update check.")
            recommendations.append("Check for updates manually.")
    except Exception as e:
        report.append(f"⚠️ Update check failed: {e}")

def check_world_writable():
    global score, max_score
    max_score += 1
    try:
        output = subprocess.getoutput("find / -xdev -type f -perm -0002 2>/dev/null")
        if output.strip():
            report.append("❌ World-writable files found:\n" + output)
            recommendations.append("Review and remove world-writable permissions where not needed.")
        else:
            report.append("✅ No world-writable files found.")
            score += 1
    except Exception as e:
        report.append(f"⚠️ World-writable file check failed: {e}")

def check_open_ports():
    global score, max_score
    max_score += 1
    try:
        output = subprocess.getoutput("ss -tuln | grep -v '127.0.0.1' | grep -v '::1' | grep -v 'State'")
        if output.strip():
            report.append("⚠️ The following services are listening on non-localhost addresses:\n" + output)
            recommendations.append("Review open ports and disable unnecessary services.")
        else:
            report.append("✅ No unnecessary network services listening externally.")
            score += 1
    except Exception as e:
        report.append(f"⚠️ Open ports check failed: {e}")

def check_sudoers():
    global score, max_score
    max_score += 1
    sudoers_file = "/etc/sudoers"
    try:
        with open(sudoers_file, "r") as f:
            lines = f.readlines()
        risky = [line for line in lines if "ALL=(ALL) NOPASSWD:ALL" in line and not line.strip().startswith("#")]
        if risky:
            report.append("❌ Insecure sudoers entries found:\n" + "".join(risky))
            recommendations.append("Remove NOPASSWD:ALL from /etc/sudoers unless absolutely necessary.")
        else:
            report.append("✅ Sudoers file looks secure.")
            score += 1
    except Exception as e:
        report.append(f"⚠️ Sudoers file check failed: {e}")

def check_empty_passwords():
    global score, max_score
    max_score += 1
    try:
        output = subprocess.getoutput("awk -F: '($2 == \"\") { print $1 }' /etc/shadow")
        if output.strip():
            report.append("❌ The following users have empty passwords:\n" + output)
            recommendations.append("Lock accounts or set passwords for accounts with empty passwords.")
        else:
            report.append("✅ No users with empty passwords.")
            score += 1
    except Exception as e:
        report.append(f"⚠️ Empty passwords check failed: {e}")

def check_cron():
    global score, max_score
    max_score += 1
    try:
        if os.path.isdir("/etc/cron.d"):
            report.append("✅ Cron jobs found and managed.")
            score += 1
        else:
            report.append("❌ Cron not properly configured.")
            recommendations.append("Ensure cron is installed and /etc/cron.d exists.")
    except Exception as e:
        report.append(f"⚠️ Cron configuration check failed: {e}")

def check_password_policy():
    global score, max_score
    max_score += 3
    try:
        with open('/etc/login.defs', 'r') as f:
            content = f.read()
        max_days = next((line.split()[1] for line in content.splitlines() if line.startswith("PASS_MAX_DAYS")), None)
        min_days = next((line.split()[1] for line in content.splitlines() if line.startswith("PASS_MIN_DAYS")), None)
        warn_age = next((line.split()[1] for line in content.splitlines() if line.startswith("PASS_WARN_AGE")), None)

        if max_days and int(max_days) <= 90:
            score += 1
            report.append("✅ PASS_MAX_DAYS is compliant (<=90).")
        else:
            report.append(f"❌ PASS_MAX_DAYS is not compliant (found: {max_days}, expected: <=90).")
            recommendations.append("Set PASS_MAX_DAYS to 90 in /etc/login.defs")

        if min_days and int(min_days) >= 7:
            score += 1
            report.append("✅ PASS_MIN_DAYS is compliant (>=7).")
        else:
            report.append(f"❌ PASS_MIN_DAYS is not compliant (found: {min_days}, expected: >=7).")
            recommendations.append("Set PASS_MIN_DAYS to 7 in /etc/login.defs")

        if warn_age and int(warn_age) >= 7:
            score += 1
            report.append("✅ PASS_WARN_AGE is compliant (>=7).")
        else:
            report.append(f"❌ PASS_WARN_AGE is not compliant (found: {warn_age}, expected: >=7).")
            recommendations.append("Set PASS_WARN_AGE to 7 in /etc/login.defs")
    except Exception as e:
        report.append(f"⚠️ Password policy check failed: {e}")

def generate_score():
    percentage = round((score / max_score) * 100, 2) if max_score else 0
    report.append(f"\n📊 Compliance Score: {score}/{max_score} ({percentage}%)")

def suggest_recommendations():
    if recommendations:
        report.append("\n🛠️ Recommendations:")
        for rec in recommendations:
            report.append(f"- {rec}")
    else:
        report.append("\n🎉 No recommendations — system looks secure!")

def write_report():
    with open("audit.txt", "w") as f:
        f.write(f"Linux Audit Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("\n\n".join(report))
    print("[+] Audit complete. Report saved to audit.txt")

# CIS Benchmark Section  #

cis_controls = [
    {
        "id": "1.1.1",
        "description": "Ensure mounting of cramfs filesystems is disabled",
        "check": lambda: "install cramfs" in subprocess.getoutput("grep cramfs /etc/modprobe.d/* 2>/dev/null"),
        "remediation": "Add 'install cramfs /bin/true' to /etc/modprobe.d/CIS.conf"
    },
    {
        "id": "2.2.1",
        "description": "Ensure time synchronization is in use (chrony or ntpd)",
        "check": lambda: any(subprocess.getoutput(f"systemctl is-active {svc}") == "active" for svc in ["chronyd", "ntpd"]),
        "remediation": "Install and enable chrony or ntpd"
    },
    {
        "id": "3.4.1",
        "description": "Ensure firewall is enabled",
        "check": lambda: (
            ("inactive" not in subprocess.getoutput("sudo ufw status").lower())
            if shutil.which("ufw")
            else ("running" in subprocess.getoutput("sudo firewall-cmd --state").lower())
            if shutil.which("firewall-cmd")
            else False
        ),
        "remediation": "Enable UFW with 'sudo ufw enable' or firewalld with 'sudo systemctl start firewalld'"
    },
    {
        "id": "5.2.8",
        "description": "Ensure SSH root login is disabled",
        "check": lambda: (
            os.path.exists("/etc/ssh/sshd_config") and
            "permitrootlogin no" in open("/etc/ssh/sshd_config").read().lower()
        ),
        "remediation": "Set 'PermitRootLogin no' in /etc/ssh/sshd_config"
    },
]

def cis_audit():
    results = []
    passed = 0
    for control in cis_controls:
        try:
            if control["check"]():
                results.append(f"{control['id']} {control['description']}: PASS")
                passed += 1
            else:
                results.append(f"{control['id']} {control['description']}: FAIL")
                results.append(f"    Remediation: {control['remediation']}")
        except Exception as e:
            results.append(f"{control['id']} {control['description']}: ERROR ({e})")
            results.append(f"    Remediation: {control['remediation']}")
    compliance = round(100 * passed / len(cis_controls), 2)
    results.append(f"\nCIS Compliance Score: {passed}/{len(cis_controls)} ({compliance}%)")
    return results

def write_cis_report(results):
    with open("cis_audit_report.txt", "w") as f:
        f.write(f"CIS Linux Benchmark Audit - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("\n".join(results))
    print("[+] CIS Audit complete. Report saved to cis_audit_report.txt")

# Main Entry Point  #

def main():
    print("[*] Starting Linux Hardening Audit (General and CIS Benchmark)...")
    # General Audit
    check_firewall()
    check_auditd()            
    check_ssh()
    check_permissions()
    check_rootkits()
    check_updates()
    check_world_writable()
    check_open_ports()
    check_sudoers()
    check_empty_passwords()   
    check_cron()              
    check_password_policy()   
    generate_score()
    suggest_recommendations()
    write_report()
  
    # CIS Audit
    results = cis_audit()
    write_cis_report(results)

if __name__ == "__main__":
    main()
