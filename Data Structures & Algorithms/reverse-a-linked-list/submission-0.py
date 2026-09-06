# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur: 				    #value on RHS of = appears in LHS next line, 4 lines
            tmp = cur.next					#hold original cur.next value
            cur.next = prev					#change cur.next
            prev = cur
            cur = tmp						#use original cur.next value
                                    
        return prev	
