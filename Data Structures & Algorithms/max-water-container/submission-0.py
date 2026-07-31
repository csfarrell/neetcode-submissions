class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_height = 0
        while l < r:
            height = (r - l) * min(heights[l], heights[r])
            print(height)
            if max_height < height:
                max_height = height
            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
        return max_height