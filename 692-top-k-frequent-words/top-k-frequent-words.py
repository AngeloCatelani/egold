class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordC = Counter(words)
        # sorted_words = sorted(word_count, key=lambda word: (-word_count[word], word))
        sortedL = sorted(wordC , key=lambda word: (-wordC[word],word))
        return sortedL[:k]