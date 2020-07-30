class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def findMiddle(head: ListNode) -> ListNode:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next
        if fast and fast.next:
            slow = slow.next
            fast = fast.next
    return slow.next #后一半的起点

def reverse(head: ListNode) -> ListNode:
    cur, pre = head, None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


def isPalindrome(head: ListNode) -> bool: #反转后一半链表再逐个比较
    if not head:
        return True
    middle = findMiddle(head)
    secondHead = reverse(middle)
    while head and secondHead:
        if head.val != secondHead.val:
            return False
        head, secondHead = head.next, secondHead.next
    return True




