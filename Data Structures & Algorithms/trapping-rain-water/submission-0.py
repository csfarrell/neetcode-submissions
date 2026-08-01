class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        output = 0

        while l < r:
            if max_left < max_right:
                l = l + 1
                max_left = max(max_left, height[l])
                output += max_left - height[l]
            else:
                r = r - 1
                max_right = max(max_right, height[r])
                output += max_right - height[r]
        return output
            # check if left less than right
            # if so, increment left
            # calculate the max of left max and height of left
            # the result will be added with left max minus height of left
            # Same as the right max stuff