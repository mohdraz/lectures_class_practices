class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self.__insert(value, self.root)

    def __insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
            else:
                self.__insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self.__insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root != None:
            self.__print_tree(self.root)

    def __print_tree(self, cur_node):
        if cur_node != None:
            self.__print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self.__print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            # return self.__height(self, self.root, 0)
            return self.__height(self.root, 0)
        else:
            return 0

    def __height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self.__height(cur_node.left_child, cur_height+1)
        right_height = self.__height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root !=None:
            return self.__search(value, self.root)
        else:
            return False
    def __search(self, value, cur_node):
        if value==cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child !=None:
           return self.__search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child !=None:
           return self.__search(value, cur_node.right_child)
        return False





def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for __ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


tree = binary_search_tree()

tree.insert(5)
tree.insert(2)
tree.insert(8)


tree.print_tree()
print(f"tree height is {str(tree.height())} ")
print(f"result of search: {tree.search(2)} ")
print(f"result of search: {tree.search(21)} ")

# focus points

"""
singly linked lists
you can only use singly linked print something backward  working --> gninkrow
data structure --> ring buffer 
how to create methods on ring buffer
optimizing a code for better runtime --> a loop within a loop --> rewrite using if statemtne
how to test runtime ---> 

"""