import imaplib
import csv

# Email credentials and server details
IMAP_SERVER = 'imap.example.com'
USERNAME = 'your_email@example.com'
PASSWORD = 'your_password'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(USERNAME, PASSWORD)
mail.select('inbox')

# Search for all emails in the inbox
status, data = mail.search(None, 'ALL')
email_ids = data[0].split()

# List to store email addresses
email_addresses = []

# Iterate over each email
for email_id in email_ids:
    status, data = mail.fetch(email_id, '(BODY[HEADER.FIELDS (FROM)])')
    raw_email = data[0][1].decode('utf-8')
    # Parse the 'From' field to extract the email address
    from_address = raw_email.split('From: ')[1].split('\n')[0]
    email_addresses.append(from_address)

# Disconnect from the server
mail.close()
mail.logout()

# Save email addresses to a CSV file
csv_file = 'email_addresses.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email Address'])
    writer.writerows([[address] for address in email_addresses])

print(f"Email addresses scraped and saved to {csv_file} file.")
