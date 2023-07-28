class Solution:
    def isValidBST(self, node: Optional[TreeNode],low=-inf, high=inf) -> bool:
        return (not node) or ((low < node.val < high) and self.isValidBST(node.left, low, node.val)  and self.isValidBST(node.right, node.val, high))