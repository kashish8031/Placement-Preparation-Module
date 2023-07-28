class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # found what we want or there is nothing 
        if (root == p or root == q or not root): return root 

        #recursion
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q) 

        if left and right: return root    # found common ancestor 
        elif left: return left
        elif right: return right