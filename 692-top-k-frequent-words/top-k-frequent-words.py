class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # wordC = Counter(words)
        # sortedL = sorted(wordC,key=lambda word:(-wordC[word],word) )
        # return sortedL[:k]
        hashmap = Counter(words)  # Count the frequency of each word
        freq = [[] for i in range(len(words) + 1)]  # Create buckets for frequencies
        
        # Populate the frequency buckets
        for word, count in hashmap.items():
            freq[count].append(word)
        
        res = []
        
        # Iterate through the buckets in reverse order (highest frequency first)
        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                freq[i].sort()  # Sort each bucket alphabetically
                for word in freq[i]:
                    res.append(word)
                    if len(res) == k:  # Stop when we've added k words
                        return res
        
        return res  # Return the result list