class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2

            mid_el = matrix[mid // n][mid % n]
            print(mid_el)
            
            if mid_el == target:
                return True
            elif mid_el < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
            

        # for index, row in enumerate(matrix):    
        #     left, right = 0, len(row) - 1
            
        #     while left <= right:
        #         mid = left + (right - left) // 2
            
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        
        # return False