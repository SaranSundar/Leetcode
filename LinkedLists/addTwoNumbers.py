# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively,
 the algorithm above iterates at most max(m, n) times
 
 Space complexity : O(max(m,n)). The length of the new list is at most max(m,n) + max(m,n)+1.
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            current.next = ListNode(carry)

        return head.next
