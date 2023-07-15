# 206. Reverse Linked List

# Easy

# Companies:
# Flipkart
# Oracle
# Facebook
# Bloomberg
# Amazon
# Samsung
# Walmart
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

        # time complexity: O(n)
        # space complexity: O(1)