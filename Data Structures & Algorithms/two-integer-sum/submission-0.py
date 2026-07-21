class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # empty hash map, value : index
        for i, n in enumerate(nums):
            diff = target - n # checking the difference
            if diff in hashMap: # if difference in hash map, return solution
                return [hashMap[diff], i]
            hashMap[n] = i