from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        isGoingRight = True
        while queue:
            currentLevel = deque([])
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if isGoingRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            isGoingRight = not isGoingRight
            result.append(list(currentLevel))        
        return result
    