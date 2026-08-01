# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def goodNodes(self, root: TreeNode) -> int:

        if not root:

            return 0

        def dfs(node, cur_max):

            if not node:

                return 0

            count = 0

            if node.val >= cur_max:

                count = 1

            count += dfs(node.left, max(cur_max, node.val))
            count += dfs(node.right, max(cur_max, node.val))

            return count

        return dfs(root, root.val)

            

        