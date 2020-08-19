class Vertex:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

class Traversal:
    def inorder(root):
        ans=[]
        def df(n):
            if n:
                df(n.right)
                ans.append(n.value)
                df(n.left)
        df(root)
        return ans

root = Vertex(36)
root.left      = Vertex(15)
root.right     = Vertex(49)
root.left.left  = Vertex(6)
root.left.right  = Vertex(22)
root.left.right.left =Vertex(19)
root.left.right.right = Vertex(31)


print("Elements in non decreasing order:")
print(Traversal.inorder(root))
