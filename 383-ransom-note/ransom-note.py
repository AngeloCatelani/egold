class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        countR = Counter(ransomNote)
        countM = Counter(magazine)

        for i in range(len(ransomNote)):
            if countM[ransomNote[i]] >= countR[ransomNote[i]]:
                continue
            if countR[ransomNote[i]] != countM[ransomNote[i]] or ransomNote[i] not in countM:
                return False

        return True