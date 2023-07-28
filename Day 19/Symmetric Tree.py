class Solution:
     def isSymmetric(self, root):

        if root == None:
            return True
        if root.right == None and root.left == None:
            return True
        if root.right == None or root.left == None:
            return False
        if root.right.val != root.left.val:
            return False

        outer,inner=TreeNode(0),TreeNode(0)
        outer.right,outer.left=root.right.right,root.left.left
        inner.right,inner.left=root.right.left,root.left.right
        return self.isSymmetric(outer) and self.isSymmetric(inner)
