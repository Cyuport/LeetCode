class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getKthFromEnd(head: ListNode, k: int) -> ListNode:
    cnt = 0
    faster, slower = head, head
    while cnt < k:
        faster = faster.next
        cnt += 1
    while faster:
        faster = faster.next
        slower = slower.next
    return slower
    '''cnt = 1
    ptr = head
    while ptr.next:
        cnt += 1
        ptr = ptr.next
    cnt -= k
    ptr = head
    while cnt:
        ptr = ptr.next
        cnt -= 1
    return ptr'''
#用快慢双指针可以一次遍历完成

