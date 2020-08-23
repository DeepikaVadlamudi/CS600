class Vertex:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key



    def search(self, key):
        if self.val == None or self.val == key:
            return str(self.val)+" is Found"
        if key > self.val:
            return Vertex.search(self.right, key)
        return Vertex.search(self.left, key)




root = Vertex(50)
root.left      = Vertex(35)
root.right     = Vertex(78)
root.left.left  = Vertex(25)
root.left.right  = Vertex(38)
print(root.search(25))
