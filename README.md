# dns-jumper-
dns jumper with python


Step-by-Step Guide
Install necessary libraries:

On Windows, you'll need the pywin32 library to interact with the Windows API.
On Unix-like systems, you'll use standard file operations to modify the /etc/resolv.conf file.
You can install pywin32 using ```pip install pywin32```

Explanation:
Imports:

Standard libraries: os, platform, and subprocess for system operations.
winreg (only on Windows) for registry operations.
Functions:

set_dns_windows(dns_servers): Updates DNS settings in the Windows registry for the specified network adapter and refreshes network settings.
set_dns_unix(dns_servers): Updates the /etc/resolv.conf file with the new DNS servers and restarts the network service if necessary.
set_dns(dns_servers): Determines the operating system and calls the appropriate function to set the DNS servers.
Main Block:

Sets the DNS servers to Google's public DNS servers (8.8.8.8 and 8.8.4.4).
Calls set_dns(dns_servers) to update the DNS settings.

***!!!Notes:
Administrative Privileges: Changing DNS settings requires administrative privileges.
Network Adapter Name on Windows: You might need to adjust the adapter_name variable to match your specific network adapter's name.
Backup of /etc/resolv.conf: The script creates a backup of the original resolv.conf file before making changes.
Disclaimer:
Modifying network settings can affect your internet connectivity. Ensure you understand the changes being made and have a way to restore the original settings if necessary.***
