# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = dummy = ListNode(None, head)		#one before head so l.next can skip n node
        r = head						#if l, r are both at head then cant skip

        while n > 0:					#give r a lead of space of n
            r = r.next
            n -= 1

        while r:						#end r & take l along, space n remains
            l = l.next
            r = r.next

        l.next = l.next.next				#delete or skip

        return dummy.next
