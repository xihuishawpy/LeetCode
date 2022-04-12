# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif not root.left and not root.right and root.val == sum:
            return True
        return any(
            child and self.hasPathSum(child, sum - root.val)
            for child in (root.left, root.right)
        )
