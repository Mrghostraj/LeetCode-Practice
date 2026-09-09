# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow = head 
        fast = head
        prev = None 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        mid = slow 

        current = mid 
        while current:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node

        first = head 
        sec = prev
        max_val = first.val + sec.val
        while first and sec:
            max_val = max(max_val, first.val + sec.val)
            first = first.next
            sec = sec.next
        return max_val

        
            
            
        