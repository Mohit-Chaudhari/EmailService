from email_service import EmailService

if __name__ == '__main__':
    """
    EMAIL PROVIDERS USED:
        1. MAILGUN
        2. MAILJET
    """
    print('Sending an email...')
    email = EmailService()
    senders_address = "test.mail@mohit.com"
    # receivers_address = "chaudharimohit39@gmail.com, mohit.chaudhari@pubmatic.com"
    receivers_address = "chaudharimohit39@gmail.com"
    subject = "Testing email service - This is subject"
    mail_body = "Testing email service - This is body"
    print(email.send_email(sender=senders_address, receiver=receivers_address, title=subject, text=mail_body))
