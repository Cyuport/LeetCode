class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> ListNode:
    slow, fast = head, head
    if not head:
         return None
    while True:
        if not fast.next or not fast.next.next:
            return None
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    res = head
    while res != slow:
        res = res.next
        slow = slow.next
    return res
