import re
import csv

task_file = 'task3.txt'

id_pattern = r'\b\d{1,5}\b' 
name_pattern = r'[A-Z][a-z]+(?: [A-Z][a-z]+)?'  
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  
date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'  
website_pattern = r'http[s]?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' 

with open(task_file, 'r', encoding='utf-8') as file:
    text = file.read()

ids = re.findall(id_pattern, text)
names = re.findall(name_pattern, text)
emails = re.findall(email_pattern, text)
dates = re.findall(date_pattern, text)
websites = re.findall(website_pattern, text)


rows = zip(ids, names, emails, dates, websites)


output_file = 'task3_normalized.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ID', 'Name', 'Email', 'Registration Date', 'Website'])  
    csv_writer.writerows(rows)

print(f"\nNormalized data saved to '{output_file}'.")
