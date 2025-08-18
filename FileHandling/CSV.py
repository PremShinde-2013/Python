import csv

rows = [
    ["name", "score"],
    ["Prem", 92],
    ["Aditi", 88],
]

# Write CSV
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV
with open("scores.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Dict-based (column names)
with open("scores.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for rec in reader:
        print(rec["name"], rec["score"])
