class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    def reverseList(head: ListNode, k: int):
        prev = None
        current = head
        while current and k > 0:
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
            k -= 1
        return prev

    current = head
    prev = None
    while current:
        count = 0
        ptr = current
        while count < k and ptr:
            ptr = ptr.next
            count += 1
