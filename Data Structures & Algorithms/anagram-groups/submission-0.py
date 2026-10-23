class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for i, s in enumerate(strs):
            my_key = "".join(sorted(s)) 
            if my_key not in words:
                words[my_key] = []
            words[my_key].append(s)
        return list(words.values()) 