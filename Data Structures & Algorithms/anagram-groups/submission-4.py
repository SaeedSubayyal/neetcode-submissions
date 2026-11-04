class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        global_dict = {}

        for str_word in strs:

            local_dict = [0] * 26

            for ch in str_word:
                local_dict[ord(ch) - ord("a")] += 1

            key = tuple(local_dict)

            if key in global_dict:
                global_dict[key].append(str_word)
            else: 
                global_dict[key] = [str_word]

        return list(global_dict.values())