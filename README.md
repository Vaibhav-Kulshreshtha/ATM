# 🏧 KCC Bank ATM System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()

A robust, interactive command-line interface (CLI) Automated Teller Machine (ATM) simulation system built with Python. It features multi-user authentication, financial transactions, daily withdrawal limits, inter-account fund transfers, and persistent JSON-based data storage.

---

## 📌 Table of Contents

- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [Default Demo Accounts](#-default-demo-accounts)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Running the Application](#running-the-application)
- [Usage Guide](#-usage-guide)
- [Data Storage Schema](#-data-storage-schema)
- [Roadmap & Enhancements](#-roadmap--enhancements)
- [License](#-license)

---

## ✨ Features

- **🔐 Multi-User Authentication**: Secure 4-digit PIN authentication with a 3-attempt lockout mechanism.
- **📝 Account Registration**: Onboard new users directly through the CLI interface with immediate database persistence.
- **💰 Balance Inquiry**: Instant balance checks.
- **💵 Cash Deposit**: Minimum deposit threshold validation (₹100 minimum) with automatic balance increment.
- **🏧 Cash Withdrawal**: Validation against available balance and enforced daily withdrawal limits (₹20,000/day).
- **🔄 Inter-Account Fund Transfer**: Seamlessly transfer funds between registered users; automatically records transaction history for both the sender and receiver.
- **📜 Mini Statement**: View the last 5 transactions with human-readable timestamps.
- **🔑 PIN Modification**: Update your 4-digit PIN securely during an active session.
- **💾 Auto-Initializing Storage**: Persists all user accounts and transaction histories in `atm_database.json`, automatically initializing with default records if not present.

---

## 🏗 Project Architecture

```text
ATM/
├── ATM.py                     # Main application logic and CLI interface
├── atm_database.json          # Active JSON database storing accounts & transactions
├── atm_database.example.json  # Seed template with default demo accounts
├── requirements.txt           # Project environment and dependency specification
├── .gitignore                 # Standard Git ignore rules for Python
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

---

## 👤 Default Demo Accounts

The system comes pre-seeded with test accounts for immediate testing:

| Account PIN | Account Holder | Initial Balance |
| :---: | :---: | :---: |
| `1234` | Mohit | ₹10,000.00 |
| `9876` | Kartik | ₹18,000.00 |
| `2006` | Vaibhav | ₹5,000.00 |
| `5000` | Atul | ₹2,700.00 |

> **Note**: You can also select option `2` from the main menu to register a new account at any time.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8 or higher**
- No external packages required (uses Python standard libraries: `json`, `os`, `datetime`).

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vaibhav-Kulshreshtha/ATM.git
   cd ATM
   ```

2. **Verify Python installation:**
   ```bash
   python3 --version
   ```

### Running the Application

Execute the script using Python:

```bash
python3 ATM.py
```

---

## 📖 Usage Guide

When launched, the system displays the top-level welcome menu:

```text
========================================
        WELCOME TO KCC BANK ATM         
========================================
1. Login to ATM
2. Open New Account (Signup)
0. Shutdown ATM

Select an Option: 
```

Once logged in, the user dashboard provides the following options:

```text
1. Check Balance
2. Withdraw
3. Deposit
4. Change PIN
5. Mini Statement
6. Transfer Fund
7. Logout / Switch User
```

---

## 🗄 Data Storage Schema

Account details and transaction histories are stored in `atm_database.json` using the following schema:

```json
{
  "1234": {
    "name": "Mohit",
    "balance": 10000.0,
    "history": [
      "[01-Oct-2026 10:00 AM] Deposited: ₹10000.0"
    ]
  }
}
```

---

## 🔮 Roadmap & Enhancements

- [ ] Secure PIN hashing using `hashlib` or `bcrypt` instead of plaintext storage.
- [ ] Migration from flat JSON to SQLite database for concurrent access and ACID compliance.
- [ ] Graphical User Interface (GUI) using Tkinter or CustomTkinter.
- [ ] One-Time Password (OTP) verification for high-value transactions.
- [ ] Export statement to PDF or CSV format.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
