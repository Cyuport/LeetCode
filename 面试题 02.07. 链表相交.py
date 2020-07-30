class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None
    la, lb = 0, 0
    pa, pb = headA, headB
    while pa:
        la += 1
        pa = pa.next
    while pb:
        lb += 1
        pb = pb.next
    pa, pb = headA, headB
    if la < lb:
        for i in range(lb-la):
            pb = pb.next
    else:
        for i in range(la-lb):
            pa = pa.next
    while pa and pb:
        if pa == pb:
            return pa
        pa, pb = pa.next, pb.next
    return None