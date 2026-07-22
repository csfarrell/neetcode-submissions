class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            sorted_string = ''.join(sorted(s))
            output[sorted_string].append(s)
        return list(output.values())