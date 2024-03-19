from pygtrie import CharTrie

class ScrabbleWordFinder:
    def __init__(self, dictionary_file):
        self.trie = CharTrie()
        self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, 'r') as file:
            for word in file:
                word = word.strip().lower()
                if word:
                    self.trie[word] = True

    def find_words(self, letters):
        letters = letters.lower()
        results = []
        self._find_words_recursive(self.trie, '', letters, results)
        return results

    def _find_words_recursive(self, trie_node, prefix, remaining_letters, results):
        if trie_node is True:
            results.append(prefix)
            return
        if not remaining_letters:
            return
        for char, node in trie_node.iteritems():
            if char in remaining_letters:
                self._find_words_recursive(node, prefix + char, remaining_letters.replace(char, '', 1), results)

if __name__ == "__main__":
    word_finder = ScrabbleWordFinder("words.txt")

    player_letters = input("Enter your letters: ")

    valid_words = word_finder.find_words(player_letters)
    print("Welcome to Scrabble Word Finder!")

    print("Valid words You can form:")
    for word in valid_words:
        print(word)
