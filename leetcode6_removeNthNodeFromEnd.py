# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        prev = None
        slow = head
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
        # remove node at slow
        if prev == None:
            head = slow.next
        else:
            prev.next = slow.next
        slow = None
        return head
            