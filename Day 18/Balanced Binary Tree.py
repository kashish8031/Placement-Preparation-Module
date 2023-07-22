class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)!=-1
    
    def height(self,root):
        if root is None:
            return 0
        hl=self.height(root.left)
        if hl==-1:
            return -1
        hr=self.height(root.right)
        if hr==-1:
            return -1
        if abs(hl-hr)>1:
            return -1
        return 1+max(hl,hr)