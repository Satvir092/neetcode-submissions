# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:

            return TreeNode(val)

        def dfs(node):

            if val > node.val:

                if node.right:

                    return dfs(node.right)

                else:

                    return node

            if val < node.val:

                if node.left:

                    return dfs(node.left)

                else:

                    return node

        cur = root

        par = dfs(root)

        if val < par.val:

            par.left = TreeNode(val)

        else:

            par.right = TreeNode(val)

        return cur

        
        