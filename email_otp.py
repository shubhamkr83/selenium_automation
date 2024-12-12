import imaplib
import email
import re


class Otp:
    def __init__(self, username, password, imap_server):
        self.imap_server = imap_server
        self.username = username
        self.password = password

    def extract_otp_from_email(self):
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(self.imap_server)

        # Login to the email account
        mail.login(self.username, self.password)

        # Select the inbox folder
        mail.select("inbox")

        # Search for emails containing OTP (adjust search criteria as needed)
        result, data = mail.search(None, '(UNSEEN SUBJECT "OTP to access your SHAMS card benefits")')

        print(result, data[0])
        otp = None

        # Iterate over email ids
        for num in data[0].split():
            # Fetch the email by id
            result, data = mail.fetch(num, '(RFC822)')

            # Parse the email content
            msg = email.message_from_bytes(data[0][1])
            # print(type())
            # Extract OTP from email body using regular expression
            otp_match = re.search(r'\b\d{6}\b', msg.get_payload()[0].as_string())

            if otp_match:
                otp = otp_match.group()
                break

        # Logout from the email account
        mail.logout()

        return otp

    # Example usage


username1 = "automationdib@gmail.com"
password1 = "ozwg ptkc xcnq koqk"
imap_server = "imap.gmail.com"
otp = Otp(username1, password1, imap_server).extract_otp_from_email()
# otp = extract_otp_from_email(username, password, imap_server)
if otp:
    print("OTP found:", otp)
else:
    print("No OTP found in email.")
