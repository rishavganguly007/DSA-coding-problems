class TreeNode:
  data: int
  left: 'TreeNode'
  right: 'TreeNode'

  def __init__(self, val = 0, left = None, right = None):
    self.data = val
    self.left = left
    self.right = right


def preorder_traversal(node: TreeNode):
  if node == None:
    return

  print(node.data, end=' ')
  preorder_traversal(node.left)
  preorder_traversal(node.right)

# ITERATIVE pre-order traversal
def iterative_preorder_traversal(node: TreeNode):
  preorder = []
  stack = []

  stack.append(node)
  while(len(stack) != 0):
    root = stack.pop()
    preorder.append(root.data)
    if(root.right != None):
      stack.append(root.right)
    
    if root.left != None:
      stack.append(root.left)
    
  print(" iterative pre-order -> ", *preorder)
  
def inorder_traversal(node: TreeNode):
  if node ==  None:
    return
  
  inorder_traversal(node.left)
  print(node.data, end = ' ')
  inorder_traversal(node.right)
  
# ITERATIVE in-order traversal
def iterative_inorder_traversal(root: TreeNode):
  inorder = []
  stack = []
  node = root
  while(True):
    if node is not None:
      stack.append(node)
      node = node.left
    else:
      if len(stack) == 0:
        break
      node = stack.pop()
      inorder.append(node.data)
      node = node.right
  print(" iterative in-order -> ", *inorder)

def postorder_traversal(node: TreeNode):
  if node ==  None:
    return
  
  postorder_traversal(node.left)
  postorder_traversal(node.right)
  print(node.data, end = ' ')

## a verry bad approach
def breadth_first_search(node: TreeNode, level):
  if node is None:
    return

  if level == 0:
    print(node.data, end=' ')
  if node.left is not None:
    print(node.left.data, end =' ')

  if node.right is not None:
    print(node.right.data, end =' ')

  breadth_first_search(node.left, level+1)
  breadth_first_search(node.right, level+1)


treeNode = TreeNode(1)
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(5)
treeNode.right.left = TreeNode(6)
treeNode.right.right = TreeNode(7)

print("Pre-order Traversal")
preorder_traversal(treeNode)

print()
print("In-order Traversal")
inorder_traversal(treeNode)

print()
print("Post-order Traversal")
postorder_traversal(treeNode)

print()
print("breadth_first_search")
breadth_first_search(treeNode, 0)

print()
iterative_preorder_traversal(treeNode)

print()
iterative_inorder_traversal(treeNode)
