import os
import csv
from collections import defaultdict

def process_folder(root_folder):
    tag_entries = defaultdict(list)

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)

                with open(file_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)  # Skip the header row

                    for row in csv_reader:
                        tag = row[0] if row else None  # Assuming the tag is in the first column
                        if tag:
                            tag_prefix = tag.split('_')[0]
                            entry = f'Tag: {tag}\n  File: {os.path.basename(file_path)}\n'
                            tag_entries[tag_prefix].append(entry)

    return tag_entries

def write_to_text(tag_entries, output_folder='shopmapper'):
    os.makedirs(output_folder, exist_ok=True)

    for tag_prefix in sorted(tag_entries.keys()):
        output_text_path = os.path.join(output_folder, f"{tag_prefix}_output.txt")

        with open(output_text_path, 'w') as text_file:
            for entry in sorted(tag_entries[tag_prefix]):
                text_file.write(entry)
                text_file.write('\n')  # Add an extra line break between each entry
            text_file.write('\n')

        print(f"Text document saved to {output_text_path}")

if __name__ == "__main__":
    script_location = os.path.dirname(os.path.abspath(__file__))
    shopmapper_output_folder = os.path.join(script_location, 'shopmapper')

    tag_entries = process_folder(script_location)
    write_to_text(tag_entries, shopmapper_output_folder)
