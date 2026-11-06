class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(s)
        cleanedString = []
        for  ch in s:
            if ch.isalnum():
                ch = ch.lower()
                cleanedString.append(ch)
        
        i = 0
        j = len(cleanedString) - 1 

        while i != j and i < len(cleanedString)-1 and j > 0:

            if (cleanedString[i] != cleanedString[j]):
                return False
            i += 1
            j -= 1
        return True




