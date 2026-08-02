class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        output = []
        while i < len(nums):
            j = 0
            product = 1
            while j < len(nums):
                
                if j != i:
                    product = product * int(nums[j])
                j = j + 1
            else:
                j = j + 1
            output.append(product)
            i = i + 1
        return output