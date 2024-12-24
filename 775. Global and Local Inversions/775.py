from typing import List

class Solution(object):
    def isIdealPermutation(self, nums):
        numLoc = 0
        numGlo = 0

        for idx, num in enumerate(nums):
            if num > idx:
                numGlo += (num-idx)
            elif num < idx:
                numGlo += (idx-num-1)
            
            if idx < len(nums)-1 and num > nums[idx+1]:
                numLoc += 1
        
        print(numLoc, numGlo)
        return numLoc == numGlo
    
######### FUNÇÕES PARA RODAR LOCAL FORA DO LEETCODE ############
solution = Solution()
nums1 = [1, 0, 2]
print("Example 1 Result:", solution.isIdealPermutation(nums1))  # Output: true

nums2 = [1, 2, 0]
print("Example 2 Result:", solution.isIdealPermutation(nums2))  # Output: false
