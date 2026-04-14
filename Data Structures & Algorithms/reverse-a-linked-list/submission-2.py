# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or head.next is None:
            return head

        curr = head.next
        head.next = None
        temp = curr.next
        curr.next = head
        #while curr.n is not null

        if not temp:
            return curr

        while temp.next is not None:
            print(temp.val)

            prev = curr

            curr = temp
            temp = temp.next

            curr.next = prev

        prev = curr
        curr = temp
        temp.next = prev

        return curr

        