# wordlists.py

def load_wordlist(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip().lower() for line in f if line.strip()]

def load_all_wordlists():
    """
    Returns a dictionary of categorized wordlists for use in password mutation.
    Categories: prefix, suffix, baseword
    """
    return {
        'prefix': (
            load_wordlist('data/commoncredentials.txt') +
            load_wordlist('data/colors.txt') +
            load_wordlist('data/basewords/names.txt') +
            load_wordlist('data/basewords/surnames.txt')
        ),
        'suffix': (
            load_wordlist('data/zipcodes.txt') +
            load_wordlist('data/basewords/languages.txt') +
            load_wordlist('data/dates.txt')
        ),
        'baseword': (
            load_wordlist('data/basewords/books.txt') +
            load_wordlist('data/basewords/fictional.txt') +
            load_wordlist('data/basewords/cities.txt') +
            load_wordlist('data/basewords/uscities.txt') +
            load_wordlist('data/basewords/world_cities.txt') +
            load_wordlist('data/basewords/religious_terms.txt') +
            load_wordlist('data/basewords/phrases.txt')
        )
    }

if __name__ == '__main__':
    wordlists = load_all_wordlists()
    for role in ['prefix', 'suffix', 'baseword']:
        print(f"{role}: {len(wordlists[role])} entries")