import re

patterns = [
    r'^\d+$',
    r'^[A-Z][a-z]* [A-Z][a-z]*$',
    r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$',
    r'^\w*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    r'^\+\d{1}\(\d{3}\)\d{3}-\d{2}-\d{2}$',
    r'^KZ\d{20}$'
]

with open("file- NewFile.txt", "r") as f:
    lines = f.readlines()

with open("output.txt", "w") as f_out:
    for i, line in enumerate(lines):
        line = line.strip()
        if i < len(patterns):
            match = re.match(patterns[i], line)
            if match:
                f_out.write(line + '\n')
            else:
                print('Line', i+1, 'does not match')
        else:
            print('No pattern defined for line', i+1)
