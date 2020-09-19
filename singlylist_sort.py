class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None


class SinglyList:

    def __init__(self):
        self.head = None

    # time complexity - O(n)
    def add_last(self, val):
        new_node = Node(val)
        # special case: if list is empty
        if self.head is None:
            self.head = new_node  # new_node itself is first node of list
        else:  # general case: if list already have few nodes
            # traverse till last node
            traverse = self.head
            while traverse.next is not None:
                traverse = traverse.next
            # add address of new_node into last node's next
            traverse.next = new_node

    # time complexity - O(n)
    def display(self):
        print("List: ", end='')
        traverse = self.head
        while traverse is not None:
            print(traverse.data, end=", ")
            traverse = traverse.next
        print()

    def selection_sort(self):
        i = self.head
        while i is not None:
            j = i.next
            while j is not None:
                if i.data > j.data:
                    temp = i.data
                    i.data = j.data
                    j.data = temp
                j = j.next
            i = i.next

    def reverse(self):
        old_head = self.head
        self.head = None
        while old_head is not None:
            temp = old_head
            old_head = old_head.next
            temp.next = self.head
            self.head = temp

    def rec_reverse_display(self, traverse):
        if traverse is None:
            return
        self.rec_reverse_display(traverse.next)
        print(traverse.data, end=", ")

    def reverse_display(self):
        print("Rev Display: ", end='')
        self.rec_reverse_display(self.head)
        print()

    def recur_reverse(self, traverse):
        if traverse.next is None:
            self.head = traverse
            return
        self.recur_reverse(traverse.next)
        traverse.next.next = traverse
        traverse.next = None

    def rec_reverse(self):
        if self.head is not None:
            self.recur_reverse(self.head)

    def find_middle(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if slow is not None:
            return slow.data
        return 0


def main():
    l1 = SinglyList()
    l1.add_last(30)
    l1.add_last(10)
    l1.add_last(40)
    l1.add_last(20)
    l1.display()

    l1.selection_sort()
    l1.display()

    l1.reverse()
    l1.display()

    l1.reverse_display()
    l1.display()

    l1.rec_reverse()
    l1.display()

    l1.add_last(50)
    l1.display()
    res = l1.find_middle()
    print("Middle : " + str(res))


if __name__ == "__main__":
    main()
