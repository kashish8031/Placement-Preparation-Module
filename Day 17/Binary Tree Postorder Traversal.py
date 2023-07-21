class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        traveral = []
        stack = [root]
        while(len(stack) > 0):
            if stack[-1].left is not None:
                stack.append(stack[-1].left)
                stack[-2].left = None
            elif stack[-1].right is not None:
                stack.append(stack[-1].right)
                stack[-2].right = None
            else:
                traveral.append(stack.pop().val)

        return traveral