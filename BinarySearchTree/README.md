# 🧠 Binary Search Tree Problems

## ✅ Problem 98: Validate Binary Search Tree

- **Platform:** LeetCode  
- **Link:** [Leetcode 98](https://leetcode.com/problems/validate-binary-search-tree/)
- **Status:** ✅ Solved
- **Approach:** Recursive DFS with min/max range tracking  
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H), where H is the height of the tree (due to recursion)

### 🔍 Description:
Given the root of a binary tree, determine if it is a valid Binary Search Tree (BST).

A valid BST is defined as:
- The left subtree contains only nodes with keys **less than** the node's key.
- The right subtree contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

### 💡 Solution Explanation:

We recursively check each node, making sure its value lies within a valid `(min, max)` range.  
For left child → max becomes the current node value.  
For right child → min becomes the current node value.

### 🧪 Test Case Example:
```python
      10
     /  \
    5   15

Output: True
