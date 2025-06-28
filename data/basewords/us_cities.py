import unicodedata


def clean_city_name(name):
    # Normalize accented characters (é -> e, etc.)
    name = unicodedata.normalize('NFD', name)
    name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')

    # Strip surrounding quotes or odd characters
    name = name.strip("‘’'\"")

    # Lowercase
    name = name.lower()

    # Remove spaces, apostrophes, dashes, parentheses, slashes
    for char in [' ', "'", '-', '(', ')', '/']:
        name = name.replace(char, '')

    return name


def lowercase_us_cities(input_file="us-cities.txt", output_file="uscities_cleaned.txt"):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f_in:
        lines = f_in.readlines()

    with open(output_file, 'w', encoding='utf-8') as f_out:
        for line in lines:
            cleaned = clean_city_name(line.strip())
            if cleaned:
                f_out.write(cleaned + '\n')


if __name__ == "__main__":
    lowercase_us_cities()