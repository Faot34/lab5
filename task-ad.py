import re


task_file = 'task_add.txt'


date_pattern = r'\b(?:\d{4}[-/.]\d{2}[-/.]\d{2}|\d{2}[-/.]\d{2}[-/.]\d{4})\b'  
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  
website_pattern = r'http[s]?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' 

with open(task_file, 'r', encoding='utf-8') as file:
    text = file.read()

dates = re.findall(date_pattern, text)
emails = re.findall(email_pattern, text)
websites = re.findall(website_pattern, text)

print("Dates:", dates)
print("Emails:", emails)
print("Websites:", websites)


output_file = 'task_additional_results.txt'
with open(output_file, 'w', encoding='utf-8') as output:
    output.write("Dates:\n" + "\n".join(dates) + "\n\n")
    output.write("Emails:\n" + "\n".join(emails) + "\n\n")
    output.write("Websites:\n" + "\n".join(websites) + "\n")

print(f"\nResults saved to '{output_file}'.")
