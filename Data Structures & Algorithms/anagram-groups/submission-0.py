class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            sorted_strs = "".join(sorted(str));
            if sorted_strs not in groups:
                groups[sorted_strs] = []
            groups[sorted_strs].append(str)
        result = list(groups.values());
        return result