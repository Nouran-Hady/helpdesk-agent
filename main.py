# main.py
from email_client import connect_to_email, process_email
from email_utils import extract_email_content,fetch_unread_emails

def process_unread_emails():
    """Main function to fetch and process emails."""
    mail = connect_to_email()
    email_ids = fetch_unread_emails(mail)
    for email_id in email_ids:
        process_email(email_id, mail)
    print("✅ Email processing complete!")

if __name__ == "__main__":
    process_unread_emails()

