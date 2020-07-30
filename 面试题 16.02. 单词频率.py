import collections


class WordsFrequency:

    def __init__(self, book: [str]):
        self.dic = collections.defaultdict(int)
        for word in book:
            self.dic[word] += 1

    def get(self, word: str) -> int:
        return self.dic[word]