class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordC = Counter(words)
        sortedL = sorted(wordC,key=lambda word:(-wordC[word],word) )
        return sortedL[:k]