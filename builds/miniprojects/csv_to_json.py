import csv
import json

# Full path to your CSV file (use raw string to avoid unicode errors)
csv_file = r"insert-path"

# Output JSON file
json_file = r"insert-path"

# Read CSV and convert to JSON
data = []

with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

# Write JSON to file
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # ensure_ascii=False keeps Igbo characters intact

print(f"CSV data has been converted to JSON and saved to {json_file}")
