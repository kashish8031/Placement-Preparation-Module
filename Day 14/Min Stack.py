class Node:
    def __init__(self, val=None, mini=None, next=None):
        self.val = val
        self.minimum = mini
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None


    def push(self, x: int) -> None:
        if self.head is None:
            node = Node(x, x)
            self.head = node
        else:
            node = Node(x, min(x, self.head.minimum), self.head)
            self.head = node


    def pop(self) -> None:
        self.head = self.head.next


    def top(self) -> int:
        return self.head.val


    def getMin(self) -> int:
        return self.head.minimum
