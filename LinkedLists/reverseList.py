class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        nextTemp = current.next
        current.next = prev
        prev = current
        current = nextTemp
    return prev
