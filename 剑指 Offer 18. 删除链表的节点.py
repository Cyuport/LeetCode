class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(head: ListNode, val: int) -> ListNode:
    if head.val == val:
        return head.next
    p, q = head, head.next
    while q:
        if q.val == val:
            p.next = q.next
            q.next = None
            return head
        p, q = p.next, q.next
