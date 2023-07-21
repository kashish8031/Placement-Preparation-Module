class Solution:
      def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderTraversalRecursive(root, answer):
            if root is None:
                return
            inorderTraversalRecursive(root.left, answer)
            answer.append(root.val)
            inorderTraversalRecursive(root.right, answer)
            return

        answer = []
        inorderTraversalRecursive(root, answer)
        return answer