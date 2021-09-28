# setup the data structure
class Node:
    def __init__(self,data):
        self.data=data
        self.left =None
        self.right=None

# insertion --> insert at random place
def insert(root,data):
    if root == None:
        newnode=Node(data)
        return newnode

    elif data>=root.data:
        root.right=insert(root.right,data)
    else:
        root.left=insert(root.left,data)

    return root
def inorder(root):
    if root :
        inorder(root.left)
        print(root.data)
        inorder(root.right)
# retrival --> search
def search(root,data):
    if root == None:
        return None
    elif data >root.data:
        root=search(root.right,data)
    elif data <root.data:
        root=search(root.left,data)
    elif data == root.data:
        return root
    return root

root = None
for i in range(1,10):
    root=insert(root,i)

temp=search(root,23)
if temp!=None:
    print("Found")
else:
    print("Not found")
inorder(root)




