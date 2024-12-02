"""Script to help guess a word.
    Designed for use in WORDLE, 
    but should be able to be used 
    in other scenarios as well.
"""

import argparse
import re


def get_possible_words(args):
    """Process arguments passedand return a list of possible word(s)."""
    # Read the wordlist file
    with open(args.wordlist, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()

    # Filter out words of different lengths
    words = [word for word in words if len(word) == len(args.pattern)]

    # Filter out words that contain any of the unwanted letters
    for letter in args.not_contain:
        words = [word for word in words if letter not in word]

    # Filter out words that don't contain all of the required letters
    if args.does_contain is not None:
        for letter in args.does_contain:
            words = [word for word in words if letter in word]

    # Filter out words that don't match the known pattern
    pattern = args.pattern.replace('*', '.')
    words = [word for word in words if re.match(pattern, word)]

    # Process anti-patterns
    if args.anti_pattern:
        for ap in args.anti_pattern:
            letter, position = ap.split(':')
            position = int(position) - 1  # Adjusting position to be zero-indexed
            words = [word for word in words if len(word) > position and word[position] != letter]

    return words

def main():
    "Setup PARSE and produce possible list of words."
    parser = argparse.ArgumentParser()
    parser.add_argument('--wordlist', type=str, default='wordlist.txt', help='Path to the wordlist file', required=True)
    parser.add_argument('--does-contain', type=str, help='Letters that the word does contain')
    parser.add_argument('--not-contain', type=str, help='Letters that the word does not contain')
    parser.add_argument('--pattern', type=str, help='Known pattern of the word. Respects * as a wild card. e.g., "C*A**" ', required=True)
    parser.add_argument('--anti-pattern', type=str, help='Letter and position pairs where the letter should not appear, e.g., e:1', nargs='*')
    parser.add_argument('--rank', action='store_true', help='Include word ranking metric as provided by `wordfreq`', default=False)

    args = parser.parse_args()

    if args.rank:
        from wordfreq import zipf_frequency # too lazy to learn importlib right now

    possible_words = get_possible_words(args)

    for word in possible_words:
        if args.rank:
            print(word, zipf_frequency(word, 'en'))
        else:
            print(word)

if __name__ == "__main__":
    main()
