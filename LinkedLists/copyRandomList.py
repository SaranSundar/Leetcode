class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        copy = Node(head.val, head.next, None)
        copy_ref = copy

        ref = head

        map_nodes = {head: copy}

        while ref.next:
            copy_ref.next = Node(ref.next.val, ref.next.next, None)
            map_nodes[ref.next] = copy_ref.next
            copy_ref = copy_ref.next
            ref = ref.next

        ref = head
        copy_ref = copy
        while ref:
            random_ptr = ref.random
            if random_ptr in map_nodes:
                copy_ref.random = map_nodes[random_ptr]
            ref = ref.next
            copy_ref = copy_ref.next

        return copy
