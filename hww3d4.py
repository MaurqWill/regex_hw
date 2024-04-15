# Python Regular Expressions Mastery: 

# You are given a piece of code that is intended to extract email addresses from a given text. 
# However, the code contains errors and does not function as expected. Your task is to identify and correct these errors.


import re

# text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
# emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}", text)
# print(emails)


text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z]{2,}", text)
print(emails)





# Python Regular Expressions Deep Dive: Email Extraction Enhancement

# You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains 
# (e.g., 'exclude.com'). Modify the script to extract all email addresses except those from the specified domain.


text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

import re

def extract_emails(text, excluded_domain):
    # regular expression pattern for extracting email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Find all email addresses in the text
    emails = re.findall(pattern, text)
    
    # Filter out email addresses with the excluded domain
    filtered_emails = [email for email in emails if excluded_domain not in email]
    
    return filtered_emails
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
excluded_domain = 'exclude.com'
print(extract_emails(text,excluded_domain))