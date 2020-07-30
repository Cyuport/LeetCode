import collections

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDuplicateNodes(head: ListNode) -> ListNode:
    dic = collections.defaultdict(int)
    cur, pre = head, None
    while cur:
        if dic[cur.val]:
            tmp = cur.next
            pre.next = tmp
            cur.next = None
            cur = tmp
        else:
            dic[cur.val] += 1
            pre = cur
            cur = cur.next
    return head
