import re
import wordlists
from itertools import product


wordlists_dict = wordlists.load_all_wordlists()  # populates globals commoncredentials, dates, books, etc.

# Compose your mutation lists:
prefixes = list(set(wordlists_dict['prefix']))
suffixes = list(set(wordlists_dict['suffix']))
base_words = list(set(wordlists_dict['baseword']))

LEET_MAP = {
        'a': ['4', '@', '^', '/\\'],
        'b': ['8', '6', '|3', 'ß'],
        'c': ['<', '(', '{', '['],
        'd': ['|)', 'cl', '])'],
        'e': ['3', '€', '&'],
        'f': ['ph', '|=', 'ƒ'],
        'g': ['9', '6', '&'],
        'h': ['#', '|-|', '[-]'],
        'i': ['1', '!', '|', 'eye'],
        'j': ['_|', '_/', '_7'],
        'k': ['|<', '|{', 'X'],
        'l': ['1', '|', '£'],
        'm': ['^^', '/\\/\\', '|\\/|'],
        'n': ['|\\|', '/\\/', '^/'],
        'o': ['0', '()', '*'],
        'p': ['|*', '|o', '|>', '¶'],
        'q': ['0_', '9', '(,)'],
        'r': ['|2', '12', '®'],
        's': ['5', '$', 'z'],
        't': ['7', '+', "']['"],
        'u': ['|_|', '(_)', 'v'],
        'v': ['\\/'],
        'w': ['\\/\\/', 'vv', '\\^/'],
        'x': ['%', '><', '}{'],
        'y': ['`/', '¥'],
        'z': ['2', '7_', '~/_']
    }

def base_words_mutation(password, base_word_list, max_mutations=None):
    mutations = set()
    for word in base_word_list:
        for variant in [word, word + password, password + word]:
            if max_mutations is not None and len(mutations) >= max_mutations:
                return mutations
            mutations.add(variant)
    return mutations

def prefix_mutations(password, prefix_list, max_mutations=None):
    mutations = set()
    for prefix in prefix_list:
        if max_mutations is not None and len(mutations) >= max_mutations:
            break
        mutations.add(prefix + password)
    return mutations


def leetspeak_mutations(password, max_mutations=None):
    leet_map = LEET_MAP
    options = []

    for c in password:
        lower_c = c.lower()
        subs = [c]
        if lower_c in leet_map:
            subs += leet_map[lower_c][:2]  # Keep complexity low
        options.append(subs)

    all_combinations = product(*options)
    mutations = set()

    for combo in all_combinations:
        if max_mutations and len(mutations) >= max_mutations:
            break
        mutations.add(''.join(combo))

    return mutations


def capitalization_mutations(password):
    mutations = set()

    # Basic variants
    mutations.add(password.lower())
    mutations.add(password.upper())
    mutations.add(password.capitalize())

    # Title case (e.g., 'johnsmith' -> 'JohnSmith')
    if len(password) >= 2:
        title_case = ''.join(word.capitalize() for word in re.findall(r'[a-zA-Z]+', password))
        if title_case != password:
            mutations.add(title_case)

    # Toggle case (e.g., 'PaSsWoRd')
    alt = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(password))
    mutations.add(alt)

    return mutations


def suffix_mutations(password, suffix_list, max_mutations=None):
    mutations = set()
    for suffix in suffix_list:
        if max_mutations is not None and len(mutations) >= max_mutations:
            break
        mutations.add(password + suffix)
    return mutations


def mutation_engine(password, suffixes, prefixes, base_words, depth=2, max_mutations=None):
    """
    Applies multiple mutation strategies to a password, including:
    - Leetspeak substitutions
    - Capitalization variants
    - Prefix and suffix additions
    - Base word concatenation

    Parameters:
        password (str): The base password to mutate.
        suffixes (list): List of strings to use as suffixes.
        prefixes (list): List of strings to use as prefixes.
        base_words (list): List of base words for prefix/suffix pairing.
        depth (int): How many mutation layers to apply.
        max_mutations (int): Optional cap on total number of mutations.

    Returns:
        set: All unique password mutations generated.
    """
    mutation_funcs = {
        'capitalization': lambda pwd: capitalization_mutations(pwd),
        'suffix': lambda pwd: suffix_mutations(pwd, suffixes, max_mutations),
        'prefix': lambda pwd: prefix_mutations(pwd, prefixes, max_mutations),
        'base_words': lambda pwd: base_words_mutation(pwd, base_words, max_mutations),
    }

    mutations = {password}
    all_mutations = {password}

    leet_mutations = leetspeak_mutations(password, max_mutations)
    for m in leet_mutations:
        if max_mutations and len(all_mutations) >= max_mutations:
            return all_mutations
        all_mutations.add(m)
    mutations.update(leet_mutations)

    for _ in range(depth):
        new_mutations = set()

        for pwd in mutations:
            for mutate in mutation_funcs.values():
                for m in mutate(pwd):
                    if max_mutations and len(all_mutations) >= max_mutations:
                        return all_mutations
                    if m not in all_mutations:
                        new_mutations.add(m)
                        all_mutations.add(m)

        if not new_mutations:
            break

        mutations = new_mutations

    return all_mutations


# For testing purposes
if __name__ == '__main__':
    test_input = 'password'
    mutations = mutation_engine(
        password=test_input,
        suffixes=suffixes,
        prefixes=prefixes,
        base_words=base_words,
        depth=2,
        max_mutations=5000  # optional cutoff
    )

    print(f"Total mutations generated: {len(mutations)}")
    for i, pwd in enumerate(sorted(mutations)):
        if i < 5000:  # limit output
            print(pwd)