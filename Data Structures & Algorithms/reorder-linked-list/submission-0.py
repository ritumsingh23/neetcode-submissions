# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None 
        while curr:
            nextVal = curr.next
            curr.next = prev
            prev = curr
            curr = nextVal
        
        dummy = head
        while prev:
            first, second = dummy.next, prev.next
            dummy.next = prev
            prev.next = first
            dummy, prev = first, second
