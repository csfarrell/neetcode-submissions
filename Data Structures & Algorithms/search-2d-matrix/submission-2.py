class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target and target <= row[-1]:
                print(row)
                for element in row:
                    print(element)
                    if element == target:
                        return True
        return False