# 🔍 ARP Network Scanner (Python)

This simple yet effective Python tool scans devices in your local network using the ARP protocol and lists their IP-MAC pairs. It's ideal for network security tasks, penetration testing, and ethical hacking beginners.

---

## 🚀 Features

- Clean and simple interface  
- Scans a given IP range using ARP  
- Displays IP and MAC addresses of active devices  
- Uses Scapy for low-level packet crafting and analysis  
- Command-line based

---

## ⚙️ Requirements

- Python 3.x  
- [Scapy](https://scapy.net/) library

Installation:
```bash
# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install the required library
pip install scapy
```

---

## 💻 Usage

Run the script as follows:

```bash
python3 NetworkScanner.py -i 192.168.1.1/24
```

🔹 Use the `-i` or `--ipaddress` parameter to specify the target IP range.  
CIDR notation (e.g., `/24`) is recommended.

---

## 📌 Example Output

```
IP                      MAC Address
----------------------------------------
192.168.1.1             aa:bb:cc:dd:ee:ff
192.168.1.14            00:11:22:33:44:55
192.168.1.25            78:45:c4:89:6a:1e
```

---

## 🛡️ Disclaimer

🔐 This script is for **educational purposes**, **testing**, and use on **authorized networks only**. Unauthorized scanning is illegal and unethical.

---
