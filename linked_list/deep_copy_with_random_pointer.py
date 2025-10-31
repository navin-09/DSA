# test_copy_random.py
import unittest
# from random_node import Node
# from copy_random_hashmap import copy_random_list_hashmap, copy_random_list_interleave
from typing import List, Optional, Tuple

# random_node.py
from typing import Optional

class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list_hashmap(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    old_to_new = {}
    cur = head
    # create clones (nodes only)
    while cur:
        old_to_new[cur] = Node(cur.val)
        cur = cur.next

    # assign next and random
    cur = head
    while cur:
        clone = old_to_new[cur]
        clone.next = old_to_new.get(cur.next)
        clone.random = old_to_new.get(cur.random)
        cur = cur.next

    return old_to_new[head]


def copy_random_list_interleave(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    # 1) Interleave cloned nodes: A -> A' -> B -> B' -> ...
    cur = head
    while cur:
        nxt = cur.next
        clone = Node(cur.val, next=nxt)
        cur.next = clone
        cur = nxt

    # 2) Set random pointers for clones
    cur = head
    while cur:
        clone = cur.next
        clone.random = cur.random.next if cur.random else None
        cur = clone.next

    # 3) Separate the lists
    cur = head
    clone_head = head.next
    while cur:
        clone = cur.next
        cur.next = clone.next  # restore original next
        cur = cur.next
        clone.next = cur.next if cur else None  # point clone.next to next clone

    return clone_head


def build_list(vals: List[int], random_idxs: List[Optional[int]]) -> Optional[Node]:
    """
    Build a linked list from vals and random pointer indices.
    random_idxs[i] is the index that node i.random should point to (or None).
    """
    if not vals:
        return None
    nodes = [Node(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, ridx in enumerate(random_idxs):
        nodes[i].random = nodes[ridx] if (ridx is not None) else None
    return nodes[0]

def compare_deep(original: Optional[Node], clone: Optional[Node]) -> Tuple[bool, str]:
    """
    Returns (True, "") if clone is a correct deep copy of original.
    Otherwise returns (False, reason).
    Checks:
      - same length
      - same values in order
      - clone nodes are distinct objects from originals
      - clone.random points to clone's node corresponding to original.random
    """
    if original is None and clone is None:
        return True, ""
    if (original is None) != (clone is None):
        return False, "One list is None while the other isn't."

    # map original nodes to indices
    orig_to_idx = {}
    idx = 0
    cur = original
    while cur:
        orig_to_idx[cur] = idx
        cur = cur.next
        idx += 1

    # traverse clone and original together to compare structure & values
    cur_o = original
    cur_c = clone
    idx = 0
    clone_nodes = []  # to access clone nodes by index
    while cur_o and cur_c:
        if cur_o is cur_c:
            return False, f"Node at index {idx} is the same object in both lists."
        if cur_o.val != cur_c.val:
            return False, f"Value mismatch at index {idx}: original={cur_o.val}, clone={cur_c.val}"
        clone_nodes.append(cur_c)
        cur_o = cur_o.next
        cur_c = cur_c.next
        idx += 1

    if cur_o or cur_c:
        return False, "Lists have different lengths."

    # second pass: check random pointers map to equivalent clone nodes
    cur_o = original
    cur_c = clone
    i = 0
    while cur_o and cur_c:
        if cur_o.random is None:
            if cur_c.random is not None:
                return False, f"Random pointer mismatch at index {i}: original.random is None but clone.random is not."
        else:
            # original.random should map to an index and clone.random should point to clone_nodes[index]
            expected_idx = orig_to_idx.get(cur_o.random)
            if expected_idx is None:
                return False, f"Original random pointer at index {i} points to node not in original list."
            if cur_c.random is not clone_nodes[expected_idx]:
                return False, (
                    f"Random pointer mismatch at index {i}: "
                    f"expected clone.random to point to clone node at index {expected_idx}."
                )
        cur_o = cur_o.next
        cur_c = cur_c.next
        i += 1

    return True, ""

class TestCopyRandomList(unittest.TestCase):
    def run_both_impls(self, head: Optional[Node]):
        # Hashmap impl
        clone1 = copy_random_list_hashmap(head)
        ok1, reason1 = compare_deep(head, clone1)
        self.assertTrue(ok1, f"HashMap impl failed: {reason1}")

        # Interleave impl
        clone2 = copy_random_list_interleave(head)
        ok2, reason2 = compare_deep(head, clone2)
        self.assertTrue(ok2, f"Interleave impl failed: {reason2}")

        # Also ensure the two clones are independent of each other (no shared nodes)
        # walk clone1 nodes, put into set, ensure none of clone2 nodes are in that set
        s = set()
        c = clone1
        while c:
            s.add(c)
            c = c.next
        c = clone2
        while c:
            self.assertNotIn(c, s, "Two clone lists share node objects (they must be independent).")
            c = c.next

    def test_empty_list(self):
        self.run_both_impls(None)

    def test_single_node_no_random(self):
        head = build_list([1], [None])
        self.run_both_impls(head)

    def test_single_node_random_self(self):
        head = build_list([1], [0])  # random -> self
        self.run_both_impls(head)

    def test_two_nodes_cross_random(self):
        # 1 -> 2
        # 1.random -> 2
        # 2.random -> 1
        head = build_list([1, 2], [1, 0])
        self.run_both_impls(head)

    def test_three_nodes_mixed_randoms(self):
        # 1 -> 2 -> 3
        # 1.random -> 3
        # 2.random -> None
        # 3.random -> 2
        head = build_list([1, 2, 3], [2, None, 1])
        self.run_both_impls(head)

    def test_longer_random_pattern(self):
        # 0->1->2->3->4
        # randoms: 0->4, 1->3, 2->1, 3->0, 4->2
        vals = [0,1,2,3,4]
        randoms = [4,3,1,0,2]
        head = build_list(vals, randoms)
        self.run_both_impls(head)

    def test_randoms_some_none(self):
        # 1->2->3->4
        # randoms: 0->None, 1->0, 2->None, 3->2
        vals = [1,2,3,4]
        randoms = [None,0,None,2]
        head = build_list(vals, randoms)
        self.run_both_impls(head)

if __name__ == "__main__":
    unittest.main()
