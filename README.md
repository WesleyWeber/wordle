# wordle
Repo of supporting files for word guessing, specifically designed to use against Wordle.

**Anti-pattern has been added.**

Here is an example of how the script was used to guess the word 'Tardy' in 4 guesses.

`python3 wordle.py --wordlist words_alpha.txt --not-contain 'wisoue' --does-contain 'art' --pattern '*****' --anti-pattern 'r:1' 't:4' 'r:2' 't:5' 'a:1' 't:3' 'r:5'`

Here is an example of guessing the word 'Thick' in 3 guesses:
`python3 wordle.py --wordlist words_alpha.txt --not-contain 'rouec' --does-contain 'thik' --pattern 'thi*k' --anti-pattern 't:4'`

# to do
~~Add feature to filter out words where a letter exists, but not in a known spot. (e.g. the word has an E in it, but it is known the E is not in the second position)~~