import heapq


class Node:

    # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def nth_node_from_end(linked_list:Node, target_end):
    ref_pointer = linked_list
    main_pointer = linked_list
    for _ in range(1, target_end):
        ref_pointer = ref_pointer.next
        if ref_pointer is None:
            return -1
    while ref_pointer.next is not None:
        main_pointer = main_pointer.next
        ref_pointer = ref_pointer.next
    return main_pointer.data


def rotate_linked_list(linked_list:Node, k):
    if k == 0 or head is None:
        return linked_list
    curr = linked_list
    length = 1
    while curr.next is not None:
        curr = curr.next
        length += 1
    k %= length
    if k == 0:
        curr.next = None
        return head
    curr.next = head
    for _ in range(1, k):
        curr = curr.next

    new_head = curr.next
    curr.next = None
    return new_head


def reverse_linked_list_sublist(linked_list:Node, k):
    current_node = linked_list
    next_node = None
    prev_node = None
    count = 0
    # Reverse
    while (current_node is not None and count < k):
        next_node = current_node.next
        current_node.next = prev_node
        current_node = next_node
        count += 1
    if next_node is not None:
        linked_list.next = reverse_linked_list_sublist(next_node, k)

    return prev_node

def merge_sorted_linked_lists(linked_lists: list, k):
    queue = []
    for i in range(k):
        if linked_lists[i] is not None:
            heapq.heappush(queue, (linked_lists[i].data, linked_lists[i]))
            dummy = Node(0)
            tail = dummy
            while queue:
                current = heapq.heappop(queue)[1]
                tail.next = current
                tail = tail.next
                if current.next != None:
                    heapq.heappush(queue, (current.next.data, current.next))
            return dummy.next






def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == '__main__':
    head = Node(35)
    head.next = Node(15)
    head.next.next = Node(4)
    head.next.next.next = Node(20)
    print(nth_node_from_end(head, 4))

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    head = rotate_linked_list(head, 6)
    print_list(head)
    print_list(reverse_linked_list_sublist(head, 2))