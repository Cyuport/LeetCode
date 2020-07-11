class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    stepA, stepB = 0, 0
    pA, pB = headA, headB
    while pA and pB:
        pA = pA.next
        stepA += 1
        pB = pB.next
        stepB += 1
    while pA:
        pA = pA.next
        stepA += 1
    while pB:
        pB = pB.next
        stepB += 1
    if stepA > stepB:
        for i in range(stepA-stepB):
            headA = headA.next
    else:
        for i in range(stepB-stepA):
            headB = headB.next
    while headA != headB and headA and headB:
        headA, headB = headA.next, headB.next
    if headA == headB:
        return headA
    else:
        return None