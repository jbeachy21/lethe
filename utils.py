from trie import Trie
import secrets

def secure_sample(population, k):
    """Securely sample k unique elements from population using secrets."""
    if k >= len(population):
        return population[:]  # return copy if sample size >= population

    reservoir = []
    for i, item in enumerate(population):
        if i < k:
            reservoir.append(item)
        else:
            j = secrets.randbelow(i + 1)
            if j < k:
                reservoir[j] = item
    return reservoir

def load_wordlist_sample(filepath="commoncredentials.txt", sample_size=1000):
    trie = Trie()
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f if line.strip()]
    sample = secure_sample(passwords, min(sample_size, len(passwords)))
    for password in sample:
        trie.insert(password)
    return trie

def load_and_print_trie(filepath, sample_size=None):
    trie = Trie()
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = [line.strip() for line in f if line.strip()]
        if sample_size:
            lines = secure_sample(lines, min(sample_size, len(lines)))
    for word in lines:
        trie.insert(word)
    print(trie)  # This will call your __str__ method
    return trie



if __name__ == "__main__":
    load_and_print_trie("commoncredentials.txt", sample_size=20)