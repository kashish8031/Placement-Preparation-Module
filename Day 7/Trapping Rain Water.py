# 42. Trapping Rain Water

# Hard

# Companies:
# Microsoft
# Amazon
# Netflix
# Flipkart
# Oracle
# Walmart
# Facebook
# Adobe
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[0]*len(height)
        maxl,maxr=0,0
        maxright=[0]*len(height)
        result=0
        for i,a in enumerate(height):
            maxleft[i]=maxl
            if a>maxl:
                maxl=a
            maxright[-1-i]=maxr
            if height[-1-i]>maxr:
                maxr=height[-1-i]
        for i,a in enumerate(height):
            trapwater=min(maxleft[i],maxright[i])-a
            if trapwater>0:
                result+=trapwater
        return result
    
# time complexity: O(n)
# space complexity: O(n)