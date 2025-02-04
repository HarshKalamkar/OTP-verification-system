# OTP-verification-system

This is a simple Python script that generates a 6-digit OTP and sends it to a user's email for verification. It uses the `smtplib` module to send emails via Gmail.

## 🚀 Features
- Generates a secure 6-digit OTP.
- Sends OTP to the user's email using SMTP.
- Verifies user input against the generated OTP.
- Displays success or failure messages based on OTP verification.

## 📌 Prerequisites
Before running the script, ensure you have:
- Python installed (3.x recommended).
- A Gmail account with **Less Secure Apps Access** enabled or a **Google App Password**.
- Internet connectivity.

## 🔧 Setup
1. Clone this repository or copy the script:
   ```sh
   git clone <repository-url>
   
2. Navigate to the project directory:
```sh
cd otp-verification
```

3. Install required dependencies (if any):
```sh
pip install -r requirements.txt
```

🔑 Configuration
Update the script with your Gmail credentials:

```python
sender_email = "your-email@gmail.com"
sender_password = "your-app-password"
```

⚠️ Important: Use a Google App Password instead of your regular Gmail password.
You can generate it from Google App Passwords.

▶️ Usage
1) Run the script:
```sh
python otp_verification.py
```
2) Enter the recipient's email when prompted.
3) Check your email for the OTP.
4) Enter the OTP in the terminal to verify.

🛠 Error Handling
Authentication Failed: Ensure your email and app password are correct.
Email Not Sent: Check your internet connection and SMTP settings.
Incorrect OTP: Re-run the script to generate a new OTP.
