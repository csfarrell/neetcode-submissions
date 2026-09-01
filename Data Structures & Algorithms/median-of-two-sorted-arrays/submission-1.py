class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        number = nums1 + nums2
        number.sort()
        length = len(number)
        i = length // 2
        if length % 2 == 0:
            return (number[i] + number[i - 1]) / 2
        else:
            return number[i]