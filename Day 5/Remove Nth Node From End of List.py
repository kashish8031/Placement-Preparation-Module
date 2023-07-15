# 19. Remove Nth Node From End of List

# Medium

# Companies:
# Walmart
# Google
# Netflix
# Oracle
# Microsoft
# Samsung
# Adobe
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        
        for _ in range(n):
            fast = fast.next
        
        # if fast is null, then it implies that we must remove
        # the first node. Hence, we'll return the next node
        # (after the first node) as an answer.
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)