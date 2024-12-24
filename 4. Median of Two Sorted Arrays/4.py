class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2
        left = (n1 + n2 + 1) // 2
        low, high = 0, n1
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            
            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r1 = float('inf') if mid1 == n1 else nums1[mid1]
            r2 = float('inf') if mid2 == n2 else nums2[mid2]
            
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0.0


######### FUNÇÕES PARA RODAR LOCAL FORA DO LEETCODE ############  
solution = Solution()

# Exemplo 1
nums1 = [1, 3]
nums2 = [2]
print("Exemplo 1:")
print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
print(f"Output: {solution.findMedianSortedArrays(nums1, nums2)}")
print("Explanation: merged array = [1,2,3] and median is 2.\n")

# Exemplo 2
nums1 = [1, 2]
nums2 = [3, 4]
print("Exemplo 2:")
print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
print(f"Output: {solution.findMedianSortedArrays(nums1, nums2)}")
print("Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.")