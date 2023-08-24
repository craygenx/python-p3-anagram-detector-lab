# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, word_list):
        anagrams = []
        sorted_word = sorted(self.word.lower())

        for candidate in word_list:
            if candidate.lower() != self.word.lower() and sorted(candidate.lower()) == sorted_word:
                anagrams.append(candidate)
        return anagrams