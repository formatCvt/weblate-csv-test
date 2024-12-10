import csv

# Define the header row
header = ["location", "source", "target", "ID", "fuzzy", "context", "translator_comments", "developer_comments"]

# Create a list to store all rows
rows = []

# Generate 3000 rows based on the template
for i in range(1, 3001):
    # Fill in the values for each row
    location = ""
    source = f"Это текст {i}"
    target = f"Это текст {i}"
    ID = ""
    fuzzy = "FALSE"
    context = f"context_for_row_{i}"
    translator_comments = ""
    developer_comments = ""

    # Append the current row to the list
    rows.append([location, source, target, ID, fuzzy, context, translator_comments, developer_comments])

# Write the rows to a CSV file
with open('ru.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)  # Write the header row
    writer.writerows(rows)  # Write all rows to the CSV

print("CSV file generated with 3000 rows.")