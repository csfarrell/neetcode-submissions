class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][len(matrix[0]) - 1] < target:
                low = mid + 1
            else:
                break
        inlow = 0
        inhigh = len(matrix[0]) - 1
        while inlow <= inhigh:
            inmid = (inlow + inhigh) // 2
            if matrix[mid][inmid] > target:
                inhigh = inmid - 1
            elif matrix[mid][inmid] < target:
                inlow = inmid + 1
            else:
                return True
        return False