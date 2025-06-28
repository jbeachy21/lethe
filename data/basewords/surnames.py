# lowercase_surnames.py

def lowercase_file_inplace(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = [line.strip().lower() for line in f if line.strip()]

    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


# Usage
lowercase_file_inplace('surnames.txt')