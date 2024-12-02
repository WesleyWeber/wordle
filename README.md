## About
This script and english word dictionary for use in word guessing games. This script was specifically designed to use against Wordle and Wordle clones. I suppose it could also be used for games like Scrabble or Words With Friends if you do not care to have potential scores returned.

## How to Use
```
usage: wordle.py [-h]   
        --wordlist WORDLIST             
        [--does-contain DOES_CONTAIN]   
        [--not-contain NOT_CONTAIN]     
        --pattern PATTERN               
        [--anti-pattern [ANTI_PATTERN ...]]

options:
  -h, --help            show this help message and exit
  --wordlist WORDLIST   Path to the wordlist file
  --does-contain DOES_CONTAIN
                        Letters that the word does contain
  --not-contain NOT_CONTAIN
                        Letters that the word does not contain
  --pattern PATTERN     Known pattern of the word. Respects * as a wild card. e.g., "C*A**"
  --anti-pattern [ANTI_PATTERN ...]
                        Letter and position pairs where the letter should not appear, e.g., e:1
```

## Examples

Here is an example of guessing the word 'TAWNY' in 3 guesses:

`python3 wordle.py --wordlist words_alpha.txt --not-contain 'rouech' --does-contain 'wat' --pattern '*a***' --anti-pattern 't:4' 'w:1' 't:3'`

Here is an example of guessing the word 'TARDY' in 4 guesses.

`python3 wordle.py --wordlist words_alpha.txt --not-contain 'wisoue' --does-contain 'art' --pattern '*****' --anti-pattern 'r:1' 't:4' '**Anti-pattern has been added.**r:2' 't:5' 'a:1' 't:3' 'r:5'`

Here is an example of guessing the word 'THICK' in 3 guesses:

`python3 wordle.py --wordlist words_alpha.txt --not-contain 'rouec' --does-contain 'thik' --pattern 'thi*k' --anti-pattern 't:4'`

Here is an example of guessing the word 'PURGE' in 3 guesses:

`python3 wordle.py --wordlist words_alpha.txt --not-contain 'ota' --does-contain 'rueg' --pattern '****e' --anti-pattern 'r:1' 'u:3' 'r:2' 'g:3' 'u:4'`



## To Do
* Determine how to represent likelihood of word based on usage frequency common english.
   * Complete: 75%
   * Current Note: Implemented a ranking library, but currently lacks ability to sort or show 'top 5'.
