class Vertex:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

class Traversal:
    def preorder(root):
        ans=[]
        def df(n):
            if n:
                ans.append(n.value)
                df(n.left)
                df(n.right)
        df(root)
        return ans
    def inorder(root):
        ans=[]
        def df(n):
            if n:
                df(n.left)
                ans.append(n.value)
                df(n.right)
        df(root)
        return ans
    def postorder(root):
        ans=[]
        def df(n):
            if n:
                df(n.left)
                df(n.right)
                ans.append(n.value)
        df(root)
        return ans


root = Vertex(15)
root.left      = Vertex(62)
root.right     = Vertex(37)
root.left.left  = Vertex(84)
root.left.right  = Vertex(59)
print("Preorder traversal of binary tree is")
print(Traversal.preorder(root))
print(Traversal.inorder(root))
print(Traversal.postorder(root))
