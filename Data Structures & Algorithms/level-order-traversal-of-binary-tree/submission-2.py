# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:

            return []

        output = []

        queue = deque()

        queue.append(root)

        output.append([root.val])

        while queue:

            cur_list = []

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:

                    cur_list.append(node.left.val)
                    queue.append(node.left)

                if node.right:

                    cur_list.append(node.right.val)
                    queue.append(node.right)

            if cur_list:

                output.append(cur_list)

        return output

        
        