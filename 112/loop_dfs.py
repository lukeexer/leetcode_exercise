# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        
        stack = [(root, root.val)]
        
        while stack:
            node, tmp_sum = choices.pop() # Get element from the tail of the list
            
            if node.left is None and node.right is None:
                if tmp_sum == targetSum:
                    return True
            
            if node.right: # Right node should be enqueue first!!
                stack.append((node.right, tmp_sum + node.right.val))
                
            if node.left:
                stack.append((node.left, tmp_sum + node.left.val))
                
        return False
        
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
