
# Read entire file as a single string
f = open("F:/Python/FileHandling/notes.txt", "r", encoding="utf-8")
data = f.read()
f.close()

# Better: use 'with' (auto-closes, even on error)
with open("F:/Python/FileHandling/notes.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Write (overwrites file)
with open("F:/Python/FileHandling/out.txt", "w", encoding="utf-8") as f:
    f.write("Hello\nWorld\n")

# Append (adds to end)
with open("F:/Python/FileHandling/out.txt", "a", encoding="utf-8") as f:
    f.write("Another line\n")

# Read line-by-line (memory-friendly for large files)
with open("F:/Python/FileHandling/big.txt", "r", encoding="utf-8") as f:
    for line in f:
        process = line.strip()
