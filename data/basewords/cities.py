import unicodedata


def clean_city_name(name):

    # Normalize unicode accents (é -> e, ñ -> n, etc.)
    name = unicodedata.normalize('NFD', name)
    name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')  # remove accents

    # Strip leading/trailing special quotes
    name = name.strip("‘’'\"")

    # Lowercase
    name = name.lower()

    # Remove spaces, apostrophes, dashes, parentheses, slashes
    for char_to_remove in [' ', "'", '-', '(', ')', '/']:
        name = name.replace(char_to_remove, '')

    return name

def extract_and_clean_world_cities(geonames_file, output_file='world_cities_cleaned.txt'):
    cities = set()
    with open(geonames_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            parts = line.split('\t')
            if len(parts) > 1:
                city_raw = parts[1].strip()
                if city_raw:
                    city = clean_city_name(city_raw)
                    if city:
                        cities.add(city)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        for city in sorted(cities):
            f_out.write(city + '\n')


if __name__ == "__main__":
    extract_and_clean_world_cities(geonames_file="cities15000.txt")