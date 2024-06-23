"""
Game, Set, Match
estimate: 45
actual  : 25
"""
import csv
FILENAME = "wimbledon.csv"


def main():
    """
    read the FILENAME and extract the champions and their countries then print out who have won how many times and
    which country have won
    """
    champion_to_count = {}
    won_countries = []
    read_file(champion_to_count, won_countries)
    print_champions(champion_to_count)
    print_won_countries(won_countries)


def print_won_countries(won_countries):
    """take a list of won countries then sort it and print out with format"""
    won_countries.sort()
    print(f"These {len(won_countries)} countries have won Wimbledon:")
    print(', '.join(won_countries))


def print_champions(champion_to_count):
    """take a dictionary stores champions name and their win times then print it out with format"""
    print("Wimbledon Champions:")
    for key in champion_to_count:
        print(f"{key} {champion_to_count[key]}")
    print()


def read_file(champion_to_count, won_countries):
    """
    read the csv file in FILENAME extract which county won into a list and the champion and their win times into
    a dictionary
    """
    with open(FILENAME, encoding="utf-8-sig") as in_file:
        raw_data = csv.reader(in_file)
        next(raw_data)
        for data in raw_data:
            try:
                champion_to_count[data[2]] += 1
            except KeyError:
                champion_to_count[data[2]] = 1
            if data[1] not in won_countries:
                won_countries.append(data[1])


main()
