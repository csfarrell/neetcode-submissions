class Solution:
    def search(self, nums: List[int], target: int) -> int:
        output = -1
        i = 0
        for num in nums:
            print(num)
            if num == target:
                output = i
            i = i + 1
        return output