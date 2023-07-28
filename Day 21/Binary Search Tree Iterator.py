class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iter = iter(self.iterativeInorder())
        self.nextValue = -1

    def iterativeInorder(self) :
        stack = []
        curr = self.root
        while True :
            if curr is not None :
                stack.append(curr)
                curr = curr.left

            elif stack :
                curr = stack.pop()
                yield curr.val
                curr = curr.right

            else :
                break

        return -1

    def next(self) -> int:
        if self.nextValue >= 0 :
            res = self.nextValue
            self.nextValue = -1
            return res 

        else :
            return next(self.iter)

    def hasNext(self) -> bool:
        if self.nextValue >= 0 : return True
        try :
            self.nextValue = next(self.iter)
            return True
        except StopIteration :
            return False
