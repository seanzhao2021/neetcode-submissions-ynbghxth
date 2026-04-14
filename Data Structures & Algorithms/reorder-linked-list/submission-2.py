# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #first find middle of list
        mid, fast = head, head

        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next

        temp = mid.next
        mid.next = None
        mid = temp

        #reverse mid
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        mid = prev
        
        front = head
        while front and mid:
            temp1 = front.next
            temp2 = mid.next

            front.next = mid
            mid.next = temp1

            front = temp1
            mid = temp2
        


        
        



