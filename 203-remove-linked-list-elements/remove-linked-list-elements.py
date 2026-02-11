# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head:
            curr= head
            prev=None
            while curr:
                if curr.val != val:
                    prev = curr
                    curr = curr.next
                else:
                    if prev == None:
                        head = head.next
                        curr = curr.next
                    else:
                        prev.next = curr.next
                        curr = curr.next
            return head
        