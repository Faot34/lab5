import re

#file path defined
task_file = 'task1-en.txt' 

# regex for task
number_pattern = r'\b\d+(\.\d+)?\b'
word_pattern = r'\b\w{6}\b|\b\w{8}\b'

# Read file
with open(task_file, 'r', encoding='utf-8') as file:
    text = file.read()

# find matches
numbers = re.findall(number_pattern, text)
words = re.findall(word_pattern, text)

# Results
print("Numbers (both integers and fractions):", numbers)
print("Words (6 or 8 letters):", words)

# Save results to output files
with open('task1_numbers.txt', 'w', encoding='utf-8') as num_file:
    num_file.write("\n".join(numbers))

with open('task1_words.txt', 'w', encoding='utf-8') as word_file:
    word_file.write("\n".join(words))

print("\nРезультаты сохраняются в 'task1_numbers.txt' and 'task1_words.txt'.")
