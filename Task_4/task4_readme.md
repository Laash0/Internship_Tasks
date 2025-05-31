This file is being created in correspondence to **Task 4 : Setup and Use a Firewall on Windows/Linux**.

---

A firewall is a network security device—either hardware, software, or a combination—that monitors and controls incoming and outgoing network traffic based on predetermined security rules. 

Its main function is to act as a barrier between a trusted internal network and untrusted external networks (like the internet), allowing only legitimate and safe traffic while blocking potentially harmful or unauthorized access. 

Firewalls are essential for protecting networks from threats such as unauthorized access, malware, and data breaches by filtering traffic according to rules set by administrators.

---

So , the default firewall manager for my system is `firewalld` which serves as front-end to `iptables`

Since we are just testing commands , therefore we will not be using the `--permanent` flag with the commands.
This makes sure that no accidental change becomes permanent , after a reboot all the changes made will be reverted to their earlier state.

## Testing Firewalld and its commands

1. To check the status 

```
sudo firewall-cmd --state
```

2. To list all the currently active rules of the firewall

```
sudo firewall-cmd --list-all
```

3. Next step is to block a specific port , here we choose an already allowed port to block off which in this case is port `1716`.
   This port is being used by a service named _KDE Connect_ which stopped working upon disabling the port mentioned.

```
sudo firewall-cmd --remove-port=1716/tcp
```

4. Now to add a port , we pick a port which is not yet allowed in the fireall rules. In this case it is port `22` used by service SSH.

```
sudo firewall-cmd --add-port=22/tcp
```

5. To remove the added test rules , we just reverse our actions.

```
sudo firewall-cmd --add-port=1716/tcp
```

```
sudo firewall-cmd --remove-port=22/tcp
```

6. Alternatively , the better route to get rid of all the test rules is to reload the firewall.

```
sudo firewall-cmd --reload
```

## Summary



_firewalld_ uses zones and rules to filter network traffic. Each zone defines a trust level for network connections, and rules specify which services or ports are allowed or blocked within that zone.

By default, firewalld blocks all incoming connections except those explicitly permitted (such as SSH). When you add or remove rules, you are specifying what traffic is allowed or denied.

firewalld evaluates packets against its rules: if a rule allows the packet (by service, port, or rich rule), it is accepted; otherwise, it is dropped or rejected. This approach helps protect your system from unauthorized access and network attacks
.
