# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        result = ListNode(0)
        curr = result
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return result.next


    def mergeTwoListsAttemp1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        result = None
        curr = None
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                if result == None:
                    curr = p1
                    result = curr
                else:
                    curr.next = p1
                    curr = curr.next
                p1 = p1.next
            else:    
                if result == None:
                    curr = p2
                    result = curr
                else:
                    curr.next = p2
                    curr = curr.next
                p2 = p2.next
        if p1:
            curr.next = p1
        elif p2:
            curr.next = p2        
        return result