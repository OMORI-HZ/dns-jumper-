import os
import platform
import subprocess

def set_dns_windows(dns_servers):
    import winreg as reg

    adapter_name = "Ethernet"  # Change this to your network adapter name

    key = reg.OpenKey(
        reg.HKEY_LOCAL_MACHINE,
        f"SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{adapter_name}",
        0,
        reg.KEY_SET_VALUE
    )

    dns_servers_str = ",".join(dns_servers)

    reg.SetValueEx(key, "NameServer", 0, reg.REG_SZ, dns_servers_str)
    reg.CloseKey(key)

    # Refresh network settings
    subprocess.call(["ipconfig", "/flushdns"])
    subprocess.call(["ipconfig", "/renew"])


def set_dns_unix(dns_servers):
    resolv_conf_path = "/etc/resolv.conf"
    
    backup_path = f"{resolv_conf_path}.backup"
    if not os.path.exists(backup_path):
        os.rename(resolv_conf_path, backup_path)

    with open(resolv_conf_path, "w") as resolv_conf:
        for dns in dns_servers:
            resolv_conf.write(f"nameserver {dns}\n")

    # Restart the network service if required
    #dev.omori
    if platform.system() == "Linux":
        subprocess.call(["systemctl", "restart", "networking"])
    elif platform.system() == "Darwin":
        subprocess.call(["dscacheutil", "-flushcache"])
        subprocess.call(["killall", "-HUP", "mDNSResponder"])


def set_dns(dns_servers):
    os_type = platform.system()

    if os_type == "Windows":
        set_dns_windows(dns_servers)
    elif os_type in ["Linux", "Darwin"]:
        set_dns_unix(dns_servers)
    else:
        raise NotImplementedError(f"OS {os_type} is not supported.")


if __name__ == "__main__":
    dns_servers = ["8.8.8.8", "8.8.4.4"]  # Google DNS servers

    set_dns(dns_servers)
    print("DNS servers have been updated.")
