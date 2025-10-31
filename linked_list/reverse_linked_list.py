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
head1 = build_list([1, 2, 3, 4, 5])
rev1 = reverse(head1)
print("Test 1:", to_list(rev1))  # Expected [5, 4, 3, 2, 1]

# Test 2: Single element
head2 = build_list([10])
rev2 = reverse(head2)
print("Test 2:", to_list(rev2))  # Expected [10]

# Test 3: Two elements
head3 = build_list([1, 2])
rev3 = reverse(head3)
print("Test 3:", to_list(rev3))  # Expected [2, 1]

# Test 4: Empty list
head4 = build_list([])
rev4 = reverse(head4)
print("Test 4:", to_list(rev4))  # Expected []

# Test 5: Reversing twice should return original
head5 = build_list([7, 8, 9])
rev5_once = reverse(head5)
rev5_twice = reverse(rev5_once)
print("Test 5:", to_list(rev5_twice))  # Expected [7, 8, 9]
