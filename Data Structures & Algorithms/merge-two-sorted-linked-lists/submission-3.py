# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases (one list is empty)
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1


        head = ListNode()
        curr = head

        #while True
        while True:
            if not list1:
                    curr.next = list2
                    break
            if not list2:
                    curr.next = list1
                    break

            #if pointer one val is less than or equal to pointer 2 val
            if list1.val <= list2.val:
                #curr next point to 1
                #curr = curr next
                #one = one next
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            #else (two is lesser)
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        
        return head.next