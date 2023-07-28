class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxs=float('-inf')
        self.maxSum(root,self.maxs)
        return self.maxs

    def maxSum(self,root,maxs):
        if root is None:
            return 0
        ls=max(0,self.maxSum(root.left,self.maxs))
        rs=max(0,self.maxSum(root.right,self.maxs))
        self.maxs=max(self.maxs,root.val+ls+rs)
        return root.val+max(ls,rs)