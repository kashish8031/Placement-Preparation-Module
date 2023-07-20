class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans_arr=[]
        for i in nums1:
            ans = -1
            index_two = nums2.index(i)
            temp = nums2[index_two+1:]
            for j in temp:
                if j > i:
                    ans = j
                    break
            ans_arr.append(ans)
        return ans_arr