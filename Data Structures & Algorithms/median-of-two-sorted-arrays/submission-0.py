class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_size = len(nums1) + len(nums2)
        half_size = total_size // 2

        # A: smaller list
        if len(nums1) >= len(nums2):
            A, B = nums2, nums1
        else:
            A, B = nums1, nums2

        l, r = 0, len(A) - 1
        
        while True:
            cut_A = (l+r) // 2
            cut_B = half_size - cut_A - 2

            left_A = A[cut_A] if cut_A >= 0 else float("-infinity")
            right_A = A[cut_A+1] if (cut_A + 1) < len(A) else float("infinity")

            left_B = B[cut_B] if cut_B >= 0 else float("-infinity")
            right_B = B[cut_B+1] if (cut_B + 1) < len(B) else float("infinity")

            if left_A <= right_B and left_B <= right_A:
                # find correct partition, calculate mid
                if total_size % 2:
                    return min(right_A, right_B)
                else:
                    return (max(left_A, left_B) + min (right_A, right_B)) / 2
            elif left_A > right_B:
                r = cut_A - 1
            else:
                l = cut_A + 1
