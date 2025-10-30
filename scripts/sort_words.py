# Sort the words in the file ../c.md
# The first two lines are headers and should remain at the top
# Sorting should ignore case
with open("../c.md", "r", encoding="utf-8") as f:
    lines = f.readlines()
    headers = lines[:2]
    words = [line.strip() for line in lines[2:] if line.strip()]
    words.sort(key=lambda x: x.lower())
    with open("../c.md", "w", encoding="utf-8") as f:
        f.writelines(headers + [f"{word}\n" for word in words])
