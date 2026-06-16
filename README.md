# AI-Lab

Hands-on Python automation labs for Linux system administration, log analysis, and JSON processing.

---

## Overview

This repository contains beginner-friendly Python projects designed to practice:

- Python scripting
- Linux administration
- JSON handling
- Log analysis
- File operations
- Automation concepts

---

## Project Structure

```text
AI-Lab
│
├── lab1_system_info.py
├── lab2_log_analyzer.py
├── server.log
└── .gitignore
```

---

## Lab 1 - System Information Collector

File:

```text
lab1_system_info.py
```

Collects system information from Linux using shell commands:

- Hostname
- Kernel Version
- CPU Information
- Memory Information
- System Uptime

Example Output:

```json
{
    "hostname": "ubuntu-server",
    "kernel": "Linux 6.x",
    "cpu": "Intel Xeon",
    "memory": "8GB",
    "uptime": "2 days"
}
```

Run:

```bash
python3 lab1_system_info.py
```

---

## Lab 2 - Log Analyzer

File:

```text
lab2_log_analyzer.py
```

Reads a log file and categorizes entries into:

- INFO
- WARNING
- ERROR

Input File:

```text
server.log
```

Example Log:

```text
INFO Server started
WARNING High CPU usage
ERROR Disk almost full
INFO Backup completed
```

Run:

```bash
python3 lab2_log_analyzer.py
```

Example Output:

```json
{
    "error_count": 2,
    "warning_count": 2,
    "info_count": 4
}
```

---

## Requirements

- Python 3.12+
- Linux / Ubuntu

No external Python packages required.

---

## Learning Objectives

This repository demonstrates:

- Python file handling
- JSON generation
- Linux command execution
- Log parsing
- Data categorization
- Basic automation techniques

---

## Author

Manish Chawda
