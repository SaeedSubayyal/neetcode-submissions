class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        s_counter = {}
        t_counter = {}

        for ch_s, ch_t in zip(s,t):

            # t string
            if ch_t in t_counter:
                t_counter[ch_t] += 1
            else:
                t_counter[ch_t] = 1


            # s string
            if ch_s in s_counter:
                s_counter[ch_s] += 1
            else:
                s_counter[ch_s] = 1
        return s_counter == t_counter
