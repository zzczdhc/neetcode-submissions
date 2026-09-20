# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sl1 = list1
        sl2 = list2
        dummy =ListNode()
        tail = dummy

        while sl1 is not None and sl2 is not None:
            diff = sl1.val - sl2.val
            if diff<0:
                tail.next = sl1
                tail=tail.next
                sl1 = sl1.next

            elif diff >0:
                tail.next = sl2
                tail=tail.next
                sl2 = sl2.next

            else:
                tail.next = sl1
                tail = tail.next
                sl1 = sl1.next

                tail.next = sl2
                tail = tail.next
                sl2 = sl2.next

        if sl1 is not None:
            tail.next = sl1
        else:
            tail.next = sl2

        return dummy.next



