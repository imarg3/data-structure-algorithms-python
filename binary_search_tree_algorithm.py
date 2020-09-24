class Stack:
    def __init__(self):
        self.arr = list()

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def is_empty(self):
        return len(self.arr) == 0


class Queue:
    def __init__(self):
        self.arr = list()

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop(0)

    def peek(self):
        return self.arr[0]

    def is_empty(self):
        return len(self.arr) == 0


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.visited = False

    def to_string(self):
        return "Node [data=" + str(self.data) + "]"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            traverse = self.root
            while True:
                if val < traverse.data:
                    if traverse.left is None:
                        traverse.left = new_node
                        break
                    else:
                        traverse = traverse.left
                else:  # if(val >= traverse.data)
                    if traverse.right is None:
                        traverse.right = new_node
                        break
                    else:
                        traverse = traverse.right

    def rec_in_order(self, traverse):
        if traverse is None:
            return
        self.rec_in_order(traverse.left)
        print(str(traverse.data) + ", ", end='')
        self.rec_in_order(traverse.right)

    def recur_in_order(self):
        print("In : ", end='')
        self.rec_in_order(self.root)
        print()

    '''
    def find(self, val):
        traverse = self.root
        while traverse is not None:
            if val == traverse.data:
                return traverse
            if val < traverse.data:
                traverse = traverse.left
            else:  # if(val < traverse.data)
                traverse = traverse.right
        return None
    '''

    def find(self, val):
        parent = None
        traverse = self.root
        while traverse is not None:
            if val == traverse.data:
                return traverse, parent
            parent = traverse
            if val < traverse.data:
                traverse = traverse.left
            else:  # if(val < traverse.data)
                traverse = traverse.right
        return None, None

    def delete_node(self, val):
        # find the node to be deleted with its parent
        (temp, parent) = self.find(val)
        if temp is None:
            raise Exception("Node Not Found.")
        # if node has parent & child node
        if temp.left is not None and temp.right is not None:
            parent = temp
            succ = temp.right
            while succ.left is not None:
                parent = succ
                succ = succ.left
            temp.data = succ.data
            temp = succ
        # if node doesn't have left child
        if temp.left is None:
            if temp == self.root:
                self.root = temp.right
            elif temp == parent.left:
                parent.left = temp.right
            else:  # if(temp == parent.right)
                parent.right = temp.right
        # else if node doesn't have right child
        elif temp.right is None:
            if temp == self.root:
                self.root = temp.left
            elif temp == parent.left:
                parent.left = temp.left
            else:  # if(temp == parent.right)
                parent.right = temp.left

    def depth_first_search(self):
        print("DFS: ", end='')
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            traverse = s.pop()
            print(traverse.data, end=", ")
            if traverse.right is not None:
                s.push(traverse.right)
            if traverse.left is not None:
                s.push(traverse.left)
        print()

    def breadth_first_search(self):
        print("BFS: ", end='')
        q = Queue()
        q.push(self.root)
        while not q.is_empty():
            traverse = q.pop()
            print(traverse.data, end=", ")
            if traverse.left is not None:
                q.push(traverse.left)
            if traverse.right is not None:
                q.push(traverse.right)
        print()


def main():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(30)
    bst.add(10)
    bst.add(90)
    bst.add(100)
    bst.add(40)
    bst.add(70)
    bst.add(80)
    bst.add(20)
    bst.add(60)

    bst.breadth_first_search()
    bst.depth_first_search()

    bst.recur_in_order()
    bst.delete_node(90)
    bst.recur_in_order()


if __name__ == "__main__":
    main()
