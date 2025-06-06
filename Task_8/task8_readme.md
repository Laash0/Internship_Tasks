This document is created in correspondence to **Task 8 : Working and Understanding VPN**

---

# 🛡️ VPN Setup and Usage Report – ProtonVPN on EndeavourOS KDE Plasma

## 📝 System Information
- **Operating System:** EndeavourOS
- **Desktop Environment:** KDE Plasma 6.3.5
- **VPN Client:** ProtonVPN (CLI-based)

---

## 🔧 VPN Setup

### Installation Process (General Steps for Arch-Based Systems)

1.  **Create a ProtonVPN Account**
    - Visit [https://protonvpn.com](https://protonvpn.com) and sign up for a free or paid account.

2.  **Install Required Dependencies**
    In a terminal, install `openvpn` (for OpenVPN protocol), `dialog` (for CLI prompts), and `python-pip` (to install the CLI tool):
    ```bash
    sudo pacman -S openvpn dialog python-pip
    ```
    If you plan to use the WireGuard protocol, you would also need to install `wireguard-tools`:
    ```bash
    sudo pacman -S wireguard-tools
    ```

3.  **Install ProtonVPN CLI**
    Use `pip` to install the official ProtonVPN CLI tool for your user:
    ```bash
    pip install --user protonvpn-cli
    ```

4.  **Update PATH (if needed)**
    Ensure the directory where `pip` installs user-specific executables (`~/.local/bin`) is in your system's PATH. If not, add it:
    ```bash
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```
    (Note: If you use a different shell, like Zsh, you would modify `~/.zshrc` instead of `~/.bashrc`.)

5.  **Initialize ProtonVPN CLI**
    Run the setup command to configure the CLI with your account:
    ```bash
    protonvpn-cli init
    ```
    - Follow the prompts to enter your ProtonVPN credentials.
    - Select your desired plan (Free or Paid).
    - Choose your preferred VPN protocol. While OpenVPN is robust, **WireGuard** is often recommended for its speed and modern cryptography.

6.  **Connect to a Server**
    Connect to the fastest available free server:
    ```bash
    protonvpn-cli connect --fastest
    ```
    Or connect to a specific country (e.g., Netherlands) or a specific server:
    ```bash
    protonvpn-cli connect NL
    ```
    You can list available servers to choose from using `protonvpn-cli status` or `protonvpn-cli list`.

7.  **Disconnect VPN**
    To disconnect from the VPN server:
    ```bash
    protonvpn-cli disconnect
    ```

### Firewall (Kill Switch) Recommendation

For enhanced security and to prevent accidental IP leaks if the VPN connection drops, it is highly recommended to set up a firewall rule to act as a "kill switch". This ensures that all internet traffic is blocked if the VPN tunnel is not active.

Using `UFW` (Uncomplicated Firewall) as an example (install with `sudo pacman -S ufw`):

1.  **Enable UFW:**
    ```bash
    sudo ufw enable
    ```

2.  **Allow traffic only through the VPN interface and specific ports (optional, for management):**
    First, find your VPN interface name (e.g., `pvpn-ipv6leak-v4`, `tun0`) by checking `ip a` after connecting to VPN.
    ```bash
    sudo ufw default deny outgoing
    sudo ufw default deny incoming
    sudo ufw allow out on pvpn-ipv6leak-v4
    sudo ufw allow in on pvpn-ipv6leak-v4
    # Optional: Allow SSH if you connect remotely
    sudo ufw allow ssh
    # Allow traffic to your local network (adjust IP range as needed)
    sudo ufw allow out to 192.168.1.0/24
    sudo ufw allow in from 192.168.1.0/24
    ```
    This setup will block all traffic *unless* it goes through the `pvpn-ipv6leak-v4` interface. When the VPN disconnects, this interface will go down, and all external traffic will be blocked. Remember to disable these rules or allow traffic from your primary network interface (`eth0` or `wlan0`) before disconnecting the VPN if you need normal internet access without VPN.

---

## 🌐 Connection Verification

- **IP Address after VPN connection:** `169.150.218.29` (Netherlands)
- **IP Address before VPN:** Not recorded (assumed local ISP region)
- IP change verified using [whatismyipaddress.com](https://whatismyipaddress.com)

**Encryption & Privacy Checks:**
- ✅ **HTTPS Padlock Present:** Verified on multiple websites; confirms encrypted connections using TLS.
- ✅ **DNS Leak Test Passed:** All DNS queries routed through ProtonVPN servers; no leaks detected via [dnsleaktest.com](https://dnsleaktest.com).
- ✅ **VPN Tunnel Interface Active:** `proton0` interface with IP `10.2.0.2/32` and global IPv6 address `2a07:b944::2:2/128` confirmed via `ip a`. Tunnel is up and functioning securely.

All checks confirm that the VPN is routing traffic securely with encryption in place.

---

## 📶 Speed Comparison
Tests were performed on a fiber connection (speed-capped around 40 Mbps):

| Metric    | Before VPN      | After VPN       |
|-----------|-----------------|-----------------|
| Download  | 40.11 Mbps      | 37.95 Mbps      |
| Upload    | 40.28 Mbps      | 32.99 Mbps      |
| Ping (ms) | 6–7 ms          | 164–545 ms      |

Despite high latency, download/upload performance remained close to the original, likely due to the nature of the capped fiber line.

---

## 🌍 Functionality Test
Sites accessed:
- Google Search
- YouTube
- Other websites

Browse worked without any issues, though some pages took slightly longer to load. Video playback and basic search functions performed normally.

---

## 🔐 VPN Features
All standard privacy and encryption features were available in the ProtonVPN client:
- AES-256 encryption
- OpenVPN protocol
- No-log policy
- DNS leak protection

Although features like Secure Core and Tor over VPN are not available on the free plan, essential privacy protections were active.

---

## ✅ Benefits Observed
- IP address was masked, improving privacy.
- Internet usage remained mostly unaffected.
- Able to access geo-neutral content without disruption.
- Easy CLI-based usage once installed.

---

## ⚠️ Limitations Noted
- Increased ping when connected to a distant server (Netherlands).
- Occasional slow page loads.
- Detailed encryption verification beyond standard browser indicators was not performed within the scope of this report.

---

## 💬 Personal Opinion
My experience with ProtonVPN on EndeavourOS KDE Plasma has been largely positive. While a noticeable increase in ping was observed, the minimal impact on download and upload speeds, particularly on a capped fiber connection, ensures that regular internet usage remains largely unaffected. This balance between performance and enhanced privacy, achieved through IP masking and standard encryption features, makes ProtonVPN a practical and highly recommendable choice for daily Browse. It effectively fulfills its role without significantly hindering the user experience, making it a valuable tool for maintaining online privacy.

---
