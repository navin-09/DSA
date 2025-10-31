from typing import Optional

# Basic node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return True, slow.val
        return False


# ---------------- TEST UTILITIES ---------------- #

def build_list(values):
    """Builds a linked list (without cycle) and returns the head."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def create_cycle(head, pos):
    """
    Creates a cycle in the linked list:
    'pos' is the index (0-based) of the node where the tail connects.
    If pos = -1, no cycle is created.
    """
    if pos == -1 or not head:
        return head
    cycle_start = None
    curr = head
    idx = 0
    while curr.next:
        if idx == pos:
            cycle_start = curr
        curr = curr.next
        idx += 1
    curr.next = cycle_start  # link last node to cycle_start
    return head


# ---------------- TEST CASES ---------------- #

s = Solution()

# 1️⃣ No cycle
head1 = build_list([1, 2, 3, 4])
print("Test 1 (no cycle):", s.hasCycle(head1))  # Expected: False

# 2️⃣ Small cycle at beginning
head2 = build_list([1, 2, 3, 4])
head2 = create_cycle(head2, 0)
print("Test 2 (cycle at node 0):", s.hasCycle(head2))  # Expected: True

# 3️⃣ Cycle in the middle
head3 = build_list([1, 2, 3, 4, 5])
head3 = create_cycle(head3, 2)
print("Test 3 (cycle at node 2):", s.hasCycle(head3))  # Expected: True

# 4️⃣ Single-node list without cycle
head4 = build_list([10])
print("Test 4 (single node no cycle):", s.hasCycle(head4))  # Expected: False

# 5️⃣ Single-node list with cycle
head5 = build_list([99])
head5.next = head5
print("Test 5 (single node with cycle):", s.hasCycle(head5))  # Expected: True

# 6️⃣ Empty list
head6 = build_list([])
print("Test 6 (empty list):", s.hasCycle(head6))  # Expected: False
