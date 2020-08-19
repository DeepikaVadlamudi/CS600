class Vertex:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        op = deque()
        nextq = deque()
        nextq.append(root)
        while nextq:
            k=[]
            for i in nextq:
                k.append(i.value)
            op.append(k)
            p=len(nextq)
            while p>0:
                r = nextq.popleft()
                if r.left:
                    nextq.append(r.left)
                if r.right:
                    nextq.append(r.right)
                p-=1

        return op
