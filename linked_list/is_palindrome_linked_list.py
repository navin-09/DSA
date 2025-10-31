# Define a simple Node for singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Function to reverse the linked list
def reverse(head):
    curr = head
    prv = None
    while curr:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt
    return prv


# Function to reverse the linked list
def is_palindrome(head):
    fast = head
    slow = head
    prv = None
    while fast and fast.next:
        prv = slow
        slow = slow.next
        fast = fast.next.next

    prv.next = None
    second_half = reverse(slow)
    first_half = head
    while first_half and second_half:
        if (first_half.val != second_half.val):
            return False
        first_half = first_half.next
        second_half = second_half.next
    if first_half is None and second_half is None:
        return True
    return False
    


    

# Helper: build linked list from Python list
def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head

# Helper: convert linked list to Python list
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------------- TEST CASES ---------------- #

# Test 1: Normal list
head1 = build_list([1, 2, 3, 4, 5,5, 4,3,2,1])
rev1 = is_palindrome(head1)
print("Test 1:", rev1)  # Expected True

# Test 1: Normal list
head1 = build_list([1, 2, 3, 4, 5])
rev1 = is_palindrome(head1)
print("Test 1:", rev1)  # Expected False

