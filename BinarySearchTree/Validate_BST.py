# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        # Helper function that checks whether current node is in valid range
        def valid(node, left, right):
            if not node:
                return True  # Empty subtree is valid

            if not (node.val > left and node.val < right):
                return False  # Current node violates BST rule

            # Recursively check left and right subtrees with updated ranges
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        # Start with full range (-inf to +inf)
        return valid(root, float('-inf'), float('inf'))


# -------------------------------
# TEST CODE BELOW
# -------------------------------

# Create a test tree:
#       10
#      /  \
#     5   15

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

# Create Solution object and test it
sol = Solution()
result = sol.isValidBST(root)

# Print the result
print("Is valid BST:", result)
