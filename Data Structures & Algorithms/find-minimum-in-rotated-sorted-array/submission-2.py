class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        target = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                target = min(target, nums[l])
                break
            mid = (l + r) // 2
            target = min(target, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid - 1
        return target


                