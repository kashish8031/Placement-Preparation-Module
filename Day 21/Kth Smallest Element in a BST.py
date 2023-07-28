class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        a=deque([root])
        result=[]
        while a:
            node=a.popleft()
            result.append(node.val)
            if node.left:
                a.append(node.left)
            if node.right:
                a.append(node.right)
        result.sort()
        return result[-1+k]
