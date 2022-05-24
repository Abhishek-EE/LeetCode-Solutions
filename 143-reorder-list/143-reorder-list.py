# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #First break the two list in the middle
        #what will be considered breaking something in the middle?
        #doesn't matter honestly adn finding the middle element in a list is an O(n) operation
        slow = head
        fast = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        curr = second_head
        Next = second_head
        prev = None
        while(Next):
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        second_head = prev
        
        curr = head
        Next = second_head
        curr_next = curr.next
        while(Next):
            curr.next = Next
            curr = Next
            Next = curr_next
            curr_next = curr.next
            
        