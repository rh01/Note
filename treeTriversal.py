class Node(object):
    def __init__(self, value):
        self.value = value
        # self.children = None
        self.right = None
        self.left = None
# Now we can begin to build our tree:


class Tree(object):
	"""docstring for Traversal"""
	def __init__(self,root):
		self.root = Node(root)
		# self.traverse_path = list()
		self.traverse_path = list()
	def preOrder_print(self,root):
		
		if root:
			self.traverse_path.append(root.value)
			self.preOrder_print(root.left)
			self.preOrder_print(root.right)
	def inOrder_print(self,root):
		
		if root:
			
			self.inOrder_print(root.left)
			self.traverse_path.append(root.value)
			self.inOrder_print(root.right)
	def postOrder_print(self,root):
		
		if root:
			
			self.postOrder_print(root.left)
			self.postOrder_print(root.right)
			self.traverse_path.append(root.value)
	def display_traversal_path(self):
		print self.traverse_path

	def cleanPath(self):
		self.traverse_path = list()


# Set up tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
# print tree.search(4)
# # Should be False
# print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
tree.preOrder_print(tree.root)
tree.display_traversal_path()
tree.cleanPath()

tree.inOrder_print(tree.root)
tree.display_traversal_path()
tree.cleanPath()


tree.postOrder_print(tree.root)
tree.display_traversal_path()
tree.cleanPath()

