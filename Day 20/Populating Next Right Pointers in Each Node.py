class Solution:
        def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
            prev = root
            cur = root
            while(prev):
                cur = prev
                while( cur ):
                    if(cur.left):
                        cur.left.next = cur.right
                        if(cur.next):
                            cur.right.next = cur.next.left
                    cur = cur.next
                prev = prev.left

            return root