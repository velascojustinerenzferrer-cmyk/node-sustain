# 🌐 NODE: SUSTAIN 
### *The Decentralized RFID Identity Hub*

**"Repurposing yesterday's e-waste for tomorrow's decentralized identity."**

---

## 🚀 Project Overview
**NODE: SUSTAIN** is an offline-first, decentralized identity hub created for **Quezon City University (QCU)**. This project addresses the global issue of electronic waste by transforming an obsolete **Smart Bro Pocket Wi-Fi** into a private, air-gapped "Ghost Network" gateway. 

Unlike traditional attendance systems that rely on public internet, **NODE: SUSTAIN** provides a secure, localized authentication environment that is resilient, private, and environmentally conscious.

---

## 🛠️ Technical Architecture
The system bridges hardware interrupts with modern web protocols to create a seamless sync between physical tags and cloud logs.

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Hardware** | Arduino Uno R3 + MFRC522 | RFID Data Capture |
| **Edge Feedback** | LCD1602A (I2C) | Instant Visual Confirmation |
| **Networking** | Smart Bro Pocket Wi-Fi | Private Intranet / DHCP Server |
| **Backend** | Python (Flask & WebSockets) | Real-time Serial Processing |
| **Database** | Google Sheets API | Cloud Data Persistence |



---

## 👥 The Development Team
* **Jairus (Lead Developer):** System Architecture, Backend Logic & Hardware Integration.
* **[Friend Name 1]:** Frontend HTML Structure & Data Presentation.
* **[Friend Name 2]:** Minimalist UI/UX Design & Responsive CSS.

---

## ♻️ STS & Sustainability Impact
As a **Science, Technology, and Society (STS)** initiative, this project explores:
1.  **E-Waste Sustainability:** Extending the lifecycle of discarded consumer networking hardware.
2.  **Digital Resilience:** Building functional tech that works in "dead zones" or during network outages.
3.  **Data Sovereignty:** Keeping student data within a private network to prevent third-party tracking.

---

## 🚦 Quick Start
1.  **Hardware:** Flash the `main.ino` sketch to the Arduino.
2.  **Network:** Connect your host machine and clients to the **Smart Bro Wi-Fi**.
3.  **Install:** Run `pip install -r requirements.txt`.
4.  **Launch:** Run `python app.py`.
5.  **Access:** Navigate to `http://[Your-IP]:5000` on any device in the network.

> **Note:** For security, the `credentials.json` file for the Google Sheets API is excluded from this repository via `.gitignore`. 

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
