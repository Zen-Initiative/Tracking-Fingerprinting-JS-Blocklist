import os

outputFile = os.path.join(os.path.dirname(__file__), 'duplicate-URLs.txt')

with open('tracking-js-high-URLs.txt', 'r', encoding="UTF8") as file1:
    with open('tracking-js-possible-URLs.txt', 'r', encoding="UTF8") as file2:
        lines1 = set(file1.readlines())
        lines2 = set(file2.readlines())
        duplicate_lines = lines1.intersection(lines2)

with open(outputFile, 'w', encoding="UTF8") as out: 
    sorted_lines = sorted(duplicate_lines)
    for line in sorted_lines:
        out.write(line + '\n')