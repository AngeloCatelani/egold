class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Create a frequency counter for the words
        word_count = Counter(words)

        # Sort the unique words first by frequency in descending order, then alphabetically
        sorted_words = sorted(word_count, key=lambda word: (-word_count[word], word))

        # Return the first k elements of the sorted list which represent the top-k frequent words
        return sorted_words[:k]