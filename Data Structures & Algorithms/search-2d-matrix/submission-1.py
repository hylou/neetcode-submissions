class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def index_to_row_and_col(index: int, n: int) -> tuple[int]:
            return (index // n, index % n)

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1

        while left <= right:
            mid = (left+right)//2
            i, j = index_to_row_and_col(mid, n)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        