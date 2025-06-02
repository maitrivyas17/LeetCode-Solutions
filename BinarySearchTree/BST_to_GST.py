# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root):
        self.running_sum = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.running_sum += node.val
            node.val = self.running_sum
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root

# Helper function to print the tree inorder
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

# Build test tree
#       5
#      / \
#     3   7

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

# Call and test
sol = Solution()
new_root = sol.bstToGst(root)
print("Inorder of updated BST:")
inorder(new_root)
