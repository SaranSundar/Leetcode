# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
    Recursive Solution
"""


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


"""
    Iterative Solution
"""


def mergeTwoListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    current = head

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return head.next
