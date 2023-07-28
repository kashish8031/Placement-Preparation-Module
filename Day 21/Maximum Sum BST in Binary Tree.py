
class Solution:
    def maxSum(self, root):
        if root == None:
            return True, 0, None, None
        isBST = False
        if (root.left == None or root.left.val < root.val) and (root.right == None or root.val < root.right.val):
            isBST = True
        minSum, maxSum = root.val, root.val

        leftBST, leftSum, leftMinSum, leftMaxSum = self.maxSum(root.left)
        if leftMinSum != None:
            if leftMaxSum < root.val:
                minSum = leftMinSum
            else:
                isBST = False

        rightBST, rightSum, rightMinSum, rightMaxSum = self.maxSum(root.right)
        if rightMaxSum != None:
            if root.val < rightMinSum:
                maxSum = rightMaxSum
            else:
                isBST = False

        if isBST and leftBST and rightBST:
            sum = root.val + leftSum + rightSum
            if sum > 0:
                self.maximum = max(sum, self.maximum)
            return True, sum, minSum, maxSum
        return False, 0, None, None

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        self.maxSum(root)
        return self.maximum