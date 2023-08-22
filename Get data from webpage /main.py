import requests
from bs4 import BeautifulSoup
import re

def extract_information(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            social_links = []
            social_patterns = ['facebook', 'linkedin', 'twitter', 'instagram']
            for pattern in social_patterns:
                links = soup.find_all(href=re.compile(pattern, re.I))
                for link in links:
                    social_links.append(link['href'])
            
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', str(soup))
            
            contact_pattern = r'(\+\d{1,2} \d{3} \d{3} \d{4})'
            contacts = re.findall(contact_pattern, str(soup))
            
            return social_links, emails, contacts
        else:
            return None, None, None
    except Exception as e:
        print("An error occurred:", e)
        return None, None, None

def main():
    url = input("Enter the website URL: ")
    social_links, emails, contacts = extract_information(url)
    
    if social_links:
        print("Social links:")
        for link in social_links:
            print(link)
    else:
        print("No social links found.")
    
    if emails:
        print("\nEmail:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")
    
    if contacts:
        print("\nContact:")
        for contact in contacts:
            print(contact)
    else:
        print("No contact details found.")

if __name__ == "__main__":
    main()
