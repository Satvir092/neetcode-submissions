# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:

            return None

        cur = head
        length = 0

        while cur:

            cur = cur.next
            length += 1
        
        k %= length

        if k == 0:

            return head
        pos = length - k - 1

        curr = head
        
        i = 0

        while i < pos:

            curr = curr.next
            i += 1

        new_head = curr.next
        next_node = curr.next
        curr.next = None

        while next_node.next:

            next_node = next_node.next

        print(next_node.val)

        next_node.next = head

        return new_head
            
        