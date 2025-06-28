import re

def extract_phrases(rockyou_path, output_path, min_length=8, max_words=3):
    phrases = set()
    with open(rockyou_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            pwd = line.strip().lower()
            if len(pwd) < min_length or not pwd.isascii():
                continue
            if re.match(r'^[a-z0-9\s\-_!?\.]+$', pwd):  # simple passphrase-ish
                words = re.findall(r'[a-z]+', pwd)
                if 1 < len(words) <= max_words:
                    phrases.add(pwd)
    with open(output_path, 'w', encoding='utf-8') as out:
        for phrase in sorted(phrases):
            out.write(phrase + '\n')

extract_phrases('rockyou.txt', 'basewords/phrases.txt')