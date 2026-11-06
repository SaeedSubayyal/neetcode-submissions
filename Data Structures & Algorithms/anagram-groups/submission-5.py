class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
      global_list = defaultdict(list)
      local_list = []
      for str_word in strs:
        local_list = [0]* 26
        for ch in str_word:
            local_list[(ord(ch) - ord("a"))] += 1

        global_list[tuple(local_list)].append(str_word)
    
      return list(global_list.values())
