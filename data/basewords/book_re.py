import csv
import re
import unicodedata

STOPWORDS = {'the', 'and', 'of', 'in', 'to', 'for', 'a', 'an', 'on', 'by'}

def clean_title(title):
    # Normalize unicode (e.g., "é" → "e")
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()

    # Strip weird spaces
    title = title.strip().replace('\xa0', ' ')

    # Extract only alpha/apostrophe words (preserve ' for now)
    parts = re.findall(r"[A-Za-z']+", title.lower())
    if not parts:
        return None

    # Join first 1–2 words
    joined = ''.join(parts[:2])

    # Remove apostrophes
    clean = joined.replace("'", "")

    # Minimum length check
    if len(clean) < 4:
        return None

    # Stopword-only check
    if clean in STOPWORDS:
        return None

    # Reject overly numeric titles (e.g., '1234')
    if sum(c.isdigit() for c in clean) > len(clean) // 2:
        return None

    return clean

def extract_classic_titles(csv_path, output_path="data/classic_books_base_words.txt", max_entries=2500):
    seen = set()
    count = 0
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        with open(output_path, "w") as out:
            for row in reader:
                title = row.get("original_title") or row.get("title")
                if not title:
                    continue
                clean = clean_title(title)
                if not clean or clean in seen:
                    continue
                # Filter short/generic names
                if len(clean) < 4:
                    continue
                seen.add(clean)
                out.write(clean + "\n")
                count += 1
                if count >= max_entries:
                    break
    print(f"✅ Saved {count} classics to {output_path}")

if __name__ == "__main__":
    extract_classic_titles(csv_path="data/basewords/books.csv")