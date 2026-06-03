Simple Multi-Threaded Port Scanner

 Description
A lightweight, multi-threaded network utility designed to scan a specified range of ports on a target IP address or hostname. This tool identifies open ports and listening services, making it useful for basic network diagnostics and security auditing. It is built entirely using Python's standard library, requiring no external dependencies.

 Features
- Multi-threaded Execution: Scans multiple ports concurrently for faster results.
- Customizable Ranges: Allows the user to specify the exact start and end ports for the scan.
- Zero Dependencies: Relies strictly on built-in Python modules (`socket`, `threading`, `datetime`).
- Clear Output: Provides real-time console feedback for open ports and a final summary upon completion.

 Prerequisites
- Python 3.x installed on your system.

 Usage
1. Download the script file (e.g., `port_scanner.py`).
2. Open a terminal or command prompt.
3. Run the script using Python:
   ```bash
   python port_scanner.py
   ```
4. Follow the on-screen prompts:
   - Host: Enter the target IP address or domain name (e.g., `127.0.0.1`).
   - Start port: Enter the lowest port number in the range (e.g., `1`).
   - End port: Enter the highest port number in the range (e.g., `1024`).

 Example Output
```text
Enter host (e.g. 127.0.0.1): 127.0.0.1
Start port: 70
End port: 85

Scanning 127.0.0.1 from port 70 to 85
Started at: 2026-06-03 22:35:00.123456

  [OPEN]   Port 80

Scan complete.
Open ports found: [80]
Finished at: 2026-06-03 22:35:01.123456
```
 Security & Authorization Disclaimer
Legal Notice: This tool is intended for educational purposes, network administration, and authorized security auditing (such as personal cyber hygiene audits). Do not use this tool to scan networks, hosts, or infrastructure for which you do not have explicit, documented permission. Unauthorized port scanning can be considered malicious activity.

 Author
Ilo C. Ejikeme
