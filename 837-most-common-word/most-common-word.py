class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap = {}
        
         # Replace punctuation with spaces
        k = "!?',;."
        for char in k:
            paragraph = paragraph.replace(char, ' ')

        # Split the paragraph into words
        arr = paragraph.split()
        # Initialize a hashmap to count the frequency of each word
        hashmap = defaultdict(int)
        for word in arr:
            lower_word = word.lower()
            hashmap[lower_word] += 1

        # Find the most common word not in the banned list
        most_common_word = ""
        max_count = 0
        for word, count in hashmap.items():
            if word not in banned and count > max_count:
                most_common_word = word
                max_count = count

        return most_common_word