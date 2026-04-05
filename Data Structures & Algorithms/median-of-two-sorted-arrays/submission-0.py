class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half_len = total_len // 2
        
        if len(B) < len(A):
            A, B = B, A
            
        left = 0
        right = len(A)
        
        while True:
            # j is the mathematically deduced partition index for B
            i = (left + right) // 2
            j = half_len - i
            
            A_left = A[i - 1] if i > 0 else float("-infinity")
            A_right = A[i] if i < len(A) else float("infinity")
            
            B_left = B[j - 1] if j > 0 else float("-infinity")
            B_right = B[j] if j < len(B) else float("infinity")
            
            if A_left <= B_right and B_left <= A_right:
                if total_len % 2 != 0:
                    return min(A_right, B_right)
                
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            # 5. If the partition is incorrect, adjust the binary search pointers
            elif A_left > B_right:
                # A's left side is too big, so we need to shrink it (move left)
                right = i - 1
            else:
                # B's left side is too big, which means A's left side is too small (move right)
                left = i + 1