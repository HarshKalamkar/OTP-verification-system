import os
import math
import random
import smtplib
import secrets

digits = "0123456789"
OTP = ''.join(secrets.choice(digits) for _ in range(6))

otp_msg = f"{OTP} is your OTP"
msg = f"Subject: OTP Verification\n\n{otp_msg}"

try:
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    
    sender_email = "[sender_EMail]"
    sender_password = "[Google app password]"

    s.login(sender_email, sender_password)

    emailid = input("Enter your email: ")
    
    s.sendmail(sender_email, emailid, msg.encode("utf-8"))
    s.quit()

    user_otp = input("Enter Your OTP >>: ")
    
    if user_otp == OTP:
        print("✅ Verified Successfully!")
    else:
        print("❌ Incorrect OTP. Please check again.")

except smtplib.SMTPAuthenticationError:
    print("❌ Authentication failed! Check your email and app password.")
except Exception as e:
    print(f"❌ Error: {e}")
