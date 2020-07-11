class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    p, curr, q = None, head, head.next
    while q:
        curr.next = p
        p = curr
        curr = q
        q = q.next
    curr.next = p
    return curr
