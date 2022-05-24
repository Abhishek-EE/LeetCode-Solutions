# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while(curr):
            length += 1
            curr = curr.next
        delete = length - n
        elem = head
        if(delete == 0):
            head = head.next
            return head
        while(delete > 1):
            delete -= 1
            elem = elem.next
        elem.next = elem.next.next
        return head
        