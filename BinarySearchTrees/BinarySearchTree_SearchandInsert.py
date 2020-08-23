class Vertex:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

    def insert(self,key):
        if self.val == None:
            self.val = key
        else:
            if key<self.val:
                if self.left == None:
                    self.left = Vertex(key)
                else:
                     self.left.insert(key)
            else:
                if self.right == None:
                    self.right = Vertex(key)
                else:
                     self.right.insert(key)
    def search(self, key):
        if self.val == None or self.val == key:
            return str(self.val)+" is Found"
        if key > self.val:
            return Vertex.search(self.right, key)
        return Vertex.search(self.left, key)




root = Vertex(50)
root.insert(35)
root.insert(25)
root.insert(28)
root.insert(78)
root.insert(38)
root.insert(54)


print(root.search(25))
