class Solution:
     def isValid(self, s):
        stack = []
        for c in list(s):
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack) <= 0 or not stack.pop() + c in ["()", "[]", "{}"]:
                    return False
        return len(stack) == 0