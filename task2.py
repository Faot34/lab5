import re

task_file = 'task2.html'

content_pattern = r'content="(.*?)"'

with open(task_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

content_matches = re.findall(content_pattern, html_content)

print("Strings inside 'content' attributes:", content_matches)

with open('task2_content_strings.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("\n".join(content_matches))

print("\nResults saved to 'task2_content_strings.txt'.")
