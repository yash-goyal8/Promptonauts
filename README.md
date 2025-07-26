# 🧠 Cognitive Companion — Agentic AI for Alzheimer’s Support

Cognitive Companion is an Agentic AI application designed to assist early-stage Alzheimer's patients with memory support, routine reminders, and emotionally comforting conversations. It can also notify loved ones via email when needed.

---

## ✨ Features

- Onboards the user and stores their routine/memory profile
- Uses Google Gemini (via Gemini API) to generate memory-aware, emotionally supportive replies
- Sets local reminders for daily routines or medications
- Sends email alerts to loved ones
- Saves user memory locally for context-aware interaction
- Secured using environment variables

---

## 🧩 Core Modules Implemented

| File           | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `planner.py`   | (To be implemented) Breaks down user goals into sub-tasks               |
| `executor.py`  | Calls Gemini API, generates responses using prompt + memory             |
| `memory.py`    | Saves and retrieves user memory (e.g., routines, meds, contacts)        |
| `tools.py`     | Contains helper functions like `set_reminder()` and `send_notification()` |
| `notifier.py`  | Sends email to emergency contacts using Gmail SMTP                      |

---

## ⚙️ Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate      # On Windows
source .venv/bin/activate   # On macOS/Linux
```

---

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 3. Configure `.env` for Gemini + Gmail

1. Get a free Gemini API key via [Google AI Studio](https://makersuite.google.com/app)
2. Create a `.env` file in the project root and add:

```env
# Gemini API Key (from Google AI Studio)
GEMINI_API_KEY=your_gemini_api_key_here

# Gmail SMTP credentials (App Password required)
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

---

### 📧 How to Set Up Gmail for Notifications

1. Go to: [https://myaccount.google.com/security](https://myaccount.google.com/security)  
   → Under "Signing in to Google", enable **2-Step Verification**

2. After enabling 2FA, go to: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)  
   → Choose **Mail** as the app and **Other (Custom name)** as the device (e.g., `Promptonauts`)  
   → Click **Generate**

3. Copy the **16-character App Password** (e.g., `abcd efgh ijkl mnop`)  
   → Paste it into `.env` like this (no spaces):

```env
EMAIL_PASSWORD=abcdefghijklmnop
```

📌 Never commit `.env` to Git. It's already in `.gitignore`.

---

### 4. Run the App

```bash
python src/main.py
```

---

### ⚠️ Disclaimer

This is a hackathon prototype and not intended for medical use without proper safety, testing, and regulatory approval.
