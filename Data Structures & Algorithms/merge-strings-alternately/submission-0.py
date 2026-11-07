class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        j = 0
        new_string = ""

        while i < len(word1) and j < len(word2):
            new_string += word1[i]
            i += 1
            new_string += word2[j]
            j += 1
        
        new_string += word1[i:]
    
        new_string += word2[j:]

        return new_string





