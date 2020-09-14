class Node:
    def __init__(self, value=0):
        self.data = value
        self.next = None


class SinglyList:
    def __init__(self):
        self.head = None

    # time complexity - O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # time complexity - O(n)
    def add_last(self, value):
        new_node = Node(value)

        # special case: if list is empty
        if self.head is None:
            self.head = new_node  # newNode itself is first node of list
        else:  # general case: if list already have few nodes
            # traverse till last node
            traverse = self.head
            while traverse.next is not None:
                traverse = traverse.next
            # add address of newNode into last node's next
            traverse.next = new_node

    # time complexity - O(n)
    def display(self):
        print("List: ", end='')
        traverse = self.head
        while traverse is not None:
            print(traverse.data, end=", ")
            traverse = traverse.next
        print()


def main():
    list1 = SinglyList()
    list1.add_last(10)
    list1.add_last(20)
    list1.add_last(30)
    list1.add_first(40)
    list1.display()


if __name__ == "__main__":
    main()
