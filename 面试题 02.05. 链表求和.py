class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:
    carry = 0
    p1, p2 = l1, l2
    if not p1:
        return p2
    if not p2:
        return p1
    while p1.next and p2.next:
        sum = p1.val + p2.val + carry
        if sum > 9:
            carry = 1
            sum -= 10
        else:
            carry = 0
        p1.val = sum
        p1, p2 = p1.next, p2.next

    sum = p1.val + p2.val + carry
    if sum > 9:
        carry = 1
        sum -= 10
    else:
        carry = 0
    p1.val = sum

    if p1.next:
        while carry and p1.next:
            p1 = p1.next
            sum = p1.val + carry
            if sum > 9:
                carry = 1
                sum -= 10
            else:
                carry = 0
            p1.val = sum
        if carry:
            p1.next = ListNode(1)
    elif p2.next:
        p1.next = p2.next
        while carry and p2.next:
            p2 = p2.next
            sum = p2.val + carry
            if sum > 9:
                carry = 1
                sum -= 10
            else:
                carry = 0
            p2.val = sum
        if carry:
            p2.next = ListNode(1)
    else:
        sum = p1.val + p2.val + carry
        if sum > 9:
            carry = 1
            sum -= 10
        else:
            carry = 0
        p1.val = sum
        if carry:
            p1.next = ListNode(1)

    return l1

