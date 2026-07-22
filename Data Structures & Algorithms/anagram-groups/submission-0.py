class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # check first one and add to list
        # if next one doesnt share any characters, add to new list
        
        output = defaultdict(list) # hashmap
        # For each string in the list, create new count
        for s in strs:
            count = [0] * 26
            # For each letter in string, add if letter found
            for c in s:
                count[ord(c) - ord("a")] += 1
            output[tuple(count)].append(s)
        return list(output.values())
