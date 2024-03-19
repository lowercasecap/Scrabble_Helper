# Scrabble Word Finder

This Python program serves as a tool to assist players in finding valid words for the game Scrabble. It utilizes a dictionary containing over 300,000 words to quickly identify valid options based on the player's available letter tiles.

## Features

- **Fast Word Lookup:** Utilizes an optimized data structure for efficient word lookup, ensuring quick response times even with a large dictionary.
- **Scrabble Rules Compliance:** Only returns words that adhere to Scrabble rules, including word length and valid characters.
- **Customizable Input:** Allows users to input their available letter tiles to generate a list of valid words.
- **User-Friendly Interface:** Designed to be easy to use, with clear instructions and prompts for user input.

## Requirements

- Python 3.12

## Installation

No installation is required. Simply clone or download the repository to your local machine to start using the Scrabble Word Finder.

Make sure you have pygtrie installed
pip install pygtrie

## Usage

1. Run the Python script `ScrabbleWordFinder.py`.
2. Input your available letter tiles when prompted.
3. The program will generate a list of valid words based on your input.
4. Choose from the list of words provided to enhance your Scrabble gameplay.

## Example

```bash
$ python scrabble_word_finder.py
Welcome to Scrabble Word Finder!

Enter your available letter tiles: rack
Valid words you can form: ['ack', 'arc', 'car', 'rack']

