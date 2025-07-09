import csv
import os

# Folder where your CSVs are located
base_dir = "/Users/Julia/Downloads/PatchWork Editions"

# List of CSV files
csv_files = [
    "translation - Sheet2.csv",
    "translation - Sheet3.csv",
    "translation - Sheet4.csv",
    "translation - Sheet5.csv",
    "translation - Sheet6.csv"
]

output_lines = []

for filename in csv_files:
    file_path = os.path.join(base_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lang = row.get('Language Code') or row.get('language') or row.get('lang') or ''
                text = row.get('Translation') or row.get('translation') or ''
                lang = lang.strip()
                text = text.strip()
                if lang and text:
                    output_lines.append(f"'{lang}': \"{text}\",")

# Write to a file
output_path = os.path.join(base_dir, "translated_output.txt")
with open(output_path, 'w', encoding='utf-8') as outfile:
    outfile.write("\n".join(output_lines))

print(f"✅ Translation file created at: {output_path}")
