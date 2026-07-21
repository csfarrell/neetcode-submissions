class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashingset = set()
        for n in nums:
            if n in hashingset:
                return True
            hashingset.add(n)
        return False
            