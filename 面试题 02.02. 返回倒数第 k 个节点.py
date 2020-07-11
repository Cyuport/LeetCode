class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def kthToLast(head: ListNode, k: int) -> int:
    cnt = 0
    cur = head
    while cur:
        cur = cur.next
        cnt += 1
    cnt -= k
    cur = head
    while cnt:
        cur = cur.next
        cnt -= 1
    return cur.val
