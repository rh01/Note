"""
Now try implementing a BST on your own. 
You'll use the same Node class as before:

This time, you'll implement search() and insert(). 
You should rewrite search() and not use your code 
from the last exercise so it takes advantage of BST
properties. Feel free to make any helper functions
you feel like you need, including the print_tree()
function from earlier for debugging. You can 
assume that two nodes with the same value won't be
inserted into the tree. 
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
    	# pass
    	if current.value < new_val:
    		if current.left:
    			self.insert_helper(cuurent.left, new_val)
    		else:
    			current.left = Node(new_val)
    	if current.value > new_val:
    		if current.right:
    			self.insert_helper(current.right, new_val)
    		else:
    			current.right = Node(new_val)
    	# return 




    def search(self, find_val):
    	return self.search_helper(self.root, find_val)

        # return False

    def search_helper(self, current, find_val):
    	if current:
	    	if current.value == find_val:
	    		return True

	    	if current.value < find_val:
	    		return self.search_helper(current.left, find_val)
	    	elif current.value > find_val:
	    		return self.search_helper(current.right, find_val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)