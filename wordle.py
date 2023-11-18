import argparse
import re

def get_possible_words(args):
    # Read the wordlist file
    with open(args.wordlist, 'r') as f:
        words = f.read().splitlines()

    # Filter out words of different lengths
    words = [word for word in words if len(word) == len(args.pattern)]
    
    # Filter out words that contain any of the unwanted letters
    for letter in args.not_contain:
        words = [word for word in words if letter not in word]
    
    # Filter out words that don't contain all of the required letters
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--wordlist', type=str, default='wordlist.txt', help='Path to the wordlist file', required=True)
    parser.add_argument('--does-contain', type=str, help='Letters that the word does contain')
    parser.add_argument('--not-contain', type=str, help='Letters that the word does not contain')
    parser.add_argument('--pattern', type=str, help='Known pattern of the word. Respects * as a wild card. e.g., "C*A**" ', required=True)
    parser.add_argument('--anti-pattern', type=str, help='Letter and position pairs where the letter should not appear, e.g., e:1', nargs='*')
    

    args = parser.parse_args()

    possible_words = get_possible_words(args)

    for word in possible_words:
        print(word)

if __name__ == "__main__":
    main()
