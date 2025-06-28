# Lethe

“The quieter you become, the more you are able to hear.”
— Ram Dass (adopted by Kali Linux)

![Lethe River](lethe.png)

## Introduction: The Myth of Lethe

In Greek mythology, **Lethe** is one of the five rivers of the underworld, known as
the River of Forgetfulness. Souls who drank from Lethe’s waters would forget their
earthly lives before reincarnation, symbolizing oblivion and the erasure of past memories.
This project is aptly named *Lethe* because it explores the mutability and transformation
of passwords — the digital "memories" we create and alter. Just as Lethe erases and reshapes
identity through forgetfulness, our mutation engine systematically alters and expands
passwords into countless variations, echoing themes of change, disguise, and concealment.



## Overview
This project implements a **mutation engine** that generates combinatorial
variations of input strings using techniques like leetspeak substitutions,
prefixes, suffixes, and capitalization patterns. The goal is to create a
versatile tool for password mutation, useful in security research and
password cracking simulations.

---

## Features
- Leetspeak mutations with controlled substitution depth
- Prefix and suffix combinations from curated wordlists
- Capitalization variations including toggle and title case
- Support for base words as prefixes or suffixes
- Configurable mutation depth and limits

---

## Usage

```python
from mutations import mutation_engine, prefixes, suffixes, base_words

input_password = "password"
mutations = mutation_engine(input_password, suffixes, prefixes, base_words,
depth=2, max_mutations=1000)

for mutation in sorted(mutations):
    print(mutation)
```

## Installation

1. **Prerequisites:**
   - Python 3.7 or higher installed on your system.
   - (Optional) It’s recommended to use a virtual environment.

2. **Clone the repository:**
3. Create and activate a virtual environment
4. Install dependencies
```bash
git clone https://github.com/yourusername/lethe.git
cd lethe
python3 -m venv lethe_venv
source lethe_venv/bin/activate
pip install -r requirements.txt
```

## Testing

python -m unittest discover tests


## Planned improvements

- Add a Flask web interface
  Build a simple web app so users can input passwords and see mutations interactively.

- Add Bootstrap to the Flask web interface

- Performance optimization
  Improve speed and memory usage for large mutation sets, possibly by using
  generators or smarter pruning.

- Support for deeper mutation depths
  Currently limited to shallow mutation depths; support configurable deeper
  recursion for more complex mutations.

- Enhanced leetspeak substitutions
  Expand and refine leetspeak mappings and allow users to customize substitutions.

- Integration with external wordlists
  Allow loading and merging of user-provided wordlists for prefixes, suffixes, and base words.

- Command-line interface (CLI)
  Add a CLI to let users run mutation generation without needing Python scripting.

- Building out the wordlists even further
  There is potential improvement especially for the phrases wordlist. Bible verses
  are a common cipher for cryptography, this is one area that the phrases
  wordlists can improve, as well as meaningful quotes from famous people and
  movies and such. Historical events could be added too.

- Unit and integration tests coverage
  Increase test coverage and add edge case tests for robustness.

- Export options
  Allow exporting results to files (txt, json) or formats compatible with
  popular password cracking tools.

- Entropy scoring and password hygiene research
  Build a password generator and with it entropy scoring to measure how secure a
  password is which can be used as another metric with all of the mutations a
  single password undergoes.

- Bloom Filter Integration
  To further optimize memory usage and speed in handling extremely large mutation sets,
  future versions may implement a Bloom filter — a probabilistic data structure
  that efficiently tests whether an element is possibly in a set. This would allow
  rapid membership checks with minimal memory footprint, at the cost of a small
  false-positive rate, enabling the mutation engine to scale better with huge
  wordlists and mutation depths.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Inspired by real-world password mutation needs and combinatorial algorithms.
- This project leverages wordlists inspired by and partially sourced from
the [SecLists](https://github.com/danielmiessler/SecLists) repository,
curated by Daniel Miessler and contributors. SecLists is an invaluable
resource in the security community, providing comprehensive wordlists for
password cracking, fuzzing, and other security testing purposes.

- Special thanks to Daniel Miessler for making these resources publicly available.


## How It Works

The mutation engine generates a comprehensive set of password variants by
applying multiple transformation strategies on an input string. The core design
uses combinatorial and layered mutations to simulate real-world password
variations often seen in password cracking and security testing.

Core Mutation Strategies
	1.	Leetspeak Substitutions
Each character in the input password is optionally replaced with visually or
semantically similar characters based on a predefined leetspeak
mapping (e.g., ‘a’ → [‘4’, ‘@’], ‘s’ → [‘5’, ‘$’]). This produces
alternative spellings commonly used by users.
	2.	Capitalization Variants
The engine generates common capitalization patterns, including lowercase,
uppercase, capitalized first letter, title case (e.g., “johnsmith” → “JohnSmith”),
and alternating caps (e.g., “PaSsWoRd”).
	3.	Prefix and Suffix Additions
Sets of common prefixes and suffixes are appended or prepended to the mutated passwords,
derived from curated wordlists. These include common numbers, words like “admin” or
“user”, and special characters.
	4.	Base Word Concatenations
Base words from wordlists can be concatenated either before or after the current password
mutation, generating additional combinations relevant to real-world password choices.

Layered Application and Depth

Mutations are applied in iterative layers defined by a configurable depth parameter. The initial input password undergoes leetspeak substitutions first, then successive rounds apply capitalization, prefixing, suffixing, and base word concatenation to all newly generated variants. This layered approach allows for complex multi-step mutations without exponential blowup in size.

Performance and Limits
	•	To manage combinatorial explosion, a max_mutations parameter caps the total
	number of mutations generated.
	•	The engine uses Python sets to ensure uniqueness and fast membership checks.
	•	Mutation functions are designed to optionally respect the max_mutations
	cap to stop generation early.

Inputs and Outputs
	•	Inputs:
	•	password (string) — the base string to mutate
	•	prefixes, suffixes, base_words (lists of strings) — curated wordlists to enhance mutations
	•	depth (int) — number of mutation iterations to apply
	•	max_mutations (int or None) — optional limit to avoid huge result sets
	•	Output:
	•	A Python set of unique password mutation strings generated by applying all mutation strategies.

Efficient Storage with Trie

To efficiently store and manage the large set of generated password mutations,
Lethe employs a Trie (prefix tree) data structure. The Trie offers several advantages:
	•	Fast insertion and lookup: Each mutation can be inserted or checked in time
	proportional to its length, which is faster than scanning large sets or lists.
	•	Memory efficiency: By sharing common prefixes among mutations, the Trie reduces
	redundant storage of repeated character sequences.
	•	Avoids duplicates naturally: The structure inherently prevents duplicate entries,
	supporting the engine’s goal of unique mutations.
	•	Supports prefix-based queries: Enables potential future features like mutation
	filtering by prefix or autocomplete capabilities.

The Trie complements Python sets used elsewhere, balancing between speed and memory usage,
especially when dealing with combinatorially large mutation sets.


## Biggest Challenges: Gathering and Curating Wordlists

One of the most significant challenges in developing *Lethe* was sourcing,
compiling, and organizing comprehensive wordlists for prefixes, suffixes,
and base words. These lists form the backbone of the mutation engine’s ability
to produce realistic and diverse password variations.

Challenges included:

- **Diversity and Quality:** Finding wordlists that contain a broad range of meaningful
prefixes and suffixes, including common patterns (like “123”, “!”, “admin”) as well as
culturally relevant or domain-specific terms.
- **Data Integration:** Combining multiple wordlists from various sources into cohesive,
deduplicated sets without losing valuable entries.
- **Maintaining Realism:** Balancing breadth with relevance to ensure mutations simulate
real-world password variations rather than producing nonsensical or unlikely results.
- **Performance Considerations:** Managing the size of the wordlists to avoid excessive
computational overhead during mutation generation.

To address these, the project integrated curated sources including common credentials,
dates, phrases, and culturally significant words, with careful preprocessing and
deduplication to optimize mutation relevance and performance.

This groundwork was critical, as the mutation engine's strength depends heavily
on the quality and comprehensiveness of the input wordlists.

---
