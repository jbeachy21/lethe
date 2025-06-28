import os


def generate_effective_dates(start_year=1950, end_year=2025):
    years = [str(y) for y in range(start_year, end_year + 1)]
    short_years = [str(y)[-2:] for y in range(start_year, end_year + 1)]

    # MMDD (limit to 01-28 to avoid invalid dates)
    mmdd = [f"{m:02}{d:02}" for m in range(1, 13) for d in range(1, 29)]

    # MMDDYYYY – just 1st of each month to keep it manageable
    mmddyyyy = [f"{m:02}01{y}" for y in range(start_year, end_year + 1)
                for m in range(1, 13)]

    # Years with symbols
    with_symbols = [f"{y}{s}" for y in years for s in ['!', '@', '#', '$']]

    # Repeated years (e.g. 19901990)
    repeated = [f"{y}{y}" for y in years]

    all_dates = set(years + short_years + mmdd + mmddyyyy + with_symbols + repeated)
    return sorted(all_dates)


def save_dates_to_file(filename="data/dates.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    dates = generate_effective_dates()
    with open(filename, "w") as f:
        for date in dates:
            f.write(date + "\n")
    print(f"✅ {len(dates)} dates written to {filename}")


if __name__ == "__main__":
    save_dates_to_file()