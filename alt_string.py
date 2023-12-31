
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        result = []
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1
            if j < len(word2):
                result.append(word2[j])
                j += 1
        return ''.join(result)

if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abc", "def"))
    print(s.mergeAlternately("abcd", "ef"))
    print(s.mergeAlternately("ab", "efgh"))
