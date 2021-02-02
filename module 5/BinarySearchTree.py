import fileinput
from collections import deque
import re


class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key, value):
        add_node = TreeNode(key, value)
        parent_node = None
        current_node = self.root
        while current_node is not None:
            parent_node = current_node
            if current_node.key < key:
                current_node = current_node.right
            elif current_node.key > key:
                current_node = current_node.left
            elif current_node.key == key:
                raise Exception('error')
        add_node.parent = parent_node
        if parent_node is None:
            self.root = add_node
        elif parent_node.key < add_node.key:
            parent_node.right = add_node
        elif parent_node.key > add_node.key:
            parent_node.left = add_node

    def delete(self, key):
        del_node = self.search_node(key)
        if del_node is None:
            raise Exception('error')
        left_child = del_node.left
        right_child = del_node.right
        if left_child is None and right_child is None:
            if del_node == self.root:
                self.root = None
            elif del_node.parent.left == del_node:
                del_node.parent.left = None
            elif del_node.parent.right == del_node:
                del_node.parent.right = None
        elif left_child is None and right_child is not None:
            if del_node == self.root:
                self.root = right_child
                right_child.parent = None
            elif del_node.parent.left == del_node:
                del_node.parent.left = right_child
                right_child.parent = del_node.parent
            elif del_node.parent.right == del_node:
                del_node.parent.right = right_child
                right_child.parent = del_node.parent
        elif left_child is not None and right_child is None:
            if del_node == self.root:
                self.root = left_child
                left_child.parent = None
            elif del_node.parent.left == del_node:
                del_node.parent.left = left_child
                left_child.parent = del_node.parent
            elif del_node.parent.right == del_node:
                del_node.parent.right = left_child
                left_child.parent = del_node.parent
        else:
            current_node = left_child
            while current_node.right is not None:
                current_node = current_node.right
            del_node.key = current_node.key
            del_node.value = current_node.value
            if current_node.left is None:
                if current_node.parent.left == current_node:
                    current_node.parent.left = None
                elif current_node.parent.right == current_node:
                    current_node.parent.right = None
                elif del_node == self.root:
                    del_node.left = None
            elif current_node.left is not None:
                if current_node.parent == del_node:
                    del_node.left = current_node.left
                    current_node.left.parent = del_node
                else:
                    current_node.parent.right = current_node.left
                    current_node.left.parent = current_node.parent

    def set(self, key, value):
        element = self.search_node(key)
        if element is None:
            raise Exception('error')
        element.value = value

    def search_node(self, key):
        current_node = self.root
        while current_node is not None and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def search(self, key):
        current_node = self.search_node(key)
        if current_node is None:
            return 0
        return '1 ' + current_node.value

    def max(self):
        current_node = self.root
        if self.root is None:
            raise Exception('error')
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def min(self):
        current_node = self.root
        if self.root is None:
            raise Exception('error')
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


def print_tree(tree, queue=None):
    if tree.root is None:
        print('_')
        return
    if queue is None:
        queue = deque()
        queue.append(tree.root)
    new_queue = deque()
    answer = ''
    has_children = False
    while len(queue) != 0:
        queue_element = queue.popleft()
        if queue_element == '_':
            new_queue.append('_')
            new_queue.append('_')
            answer += "_ "
            continue
        elif queue_element.parent is None:
            answer += '[' + str(queue_element.key) + ' ' + queue_element.value + '] '
        elif queue_element.parent is not None:
            answer += '[' + str(queue_element.key) + ' ' + queue_element.value + ' ' + str(
                queue_element.parent.key) + '] '
        if queue_element.left is not None:
            has_children = True
            new_queue.append(queue_element.left)
        else:
            new_queue.append('_')
        if queue_element.right is not None:
            has_children = True
            new_queue.append(queue_element.right)
        else:
            new_queue.append('_')
    print(answer[:-1])
    if not has_children:
        return
    print_tree(tree, new_queue)


if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()
    for line in fileinput.input():
        line = line.strip('\n')
        if re.match(r'^add [+-]?\d+ \S+$', line):
            try:
                command, element_key, element_value = line.split()
                binary_search_tree.add(int(element_key), element_value)
            except Exception as msg:
                print(msg)
        elif re.match(r'^delete [+-]?\d+$', line):
            try:
                command, element_key = line.split()
                binary_search_tree.delete(int(element_key))
            except Exception as msg:
                print(msg)
        elif re.match(r'^set [+-]?\d+ \S+$', line):
            try:
                command, element_key, element_value = line.split()
                binary_search_tree.set(int(element_key), element_value)
            except Exception as msg:
                print(msg)
        elif re.match(r'^search [+-]?\d+$', line):
            command, element_key = line.split()
            print(binary_search_tree.search(int(element_key)))
        elif re.match(r'^max$', line):
            try:
                node = binary_search_tree.max()
                print(node.key, node.value)
            except Exception as msg:
                print(msg)
        elif re.match(r'^min$', line):
            try:
                node = binary_search_tree.min()
                print(node.key, node.value)
            except Exception as msg:
                print(msg)
        elif re.match(r'^print$', line):
            print_tree(binary_search_tree)
        else:
            print('error')
