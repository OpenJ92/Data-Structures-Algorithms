class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strings:
            common = "".join(sorted(string))
            groups[common].append(string)
        return groups.values()
