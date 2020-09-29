"""
Simple Stack Implementation
"""

class Stack():
    """
    LIFO Stack
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Adds an item to the stack
        """
        self.items.append(item)

    def pop(self):
        """
        Pops an item of the stack with some validation
        """
        if self.is_empty():
            raise Exception("Can not pop an empty stack")
        return self.items.pop()

    def size(self):
        """
        Returns the size of the stack
        """
        return len(self.items)

    def is_empty(self):
        """
        Checks if there are items on the stack
        """
        return len(self.items) == 0

def main():
    stack = Stack()

    # Print the empty stack
    print(stack.items)  # print: []

    # Push item onto stack
    stack.push(5)

    # Print stack with a single item
    print(stack.items) # print: [5]

    # Push multiple items onto the stack
    stack.push(9)
    stack.push(15)
    stack.push(20)

    # Print stack with multiple items
    print(stack.items) # print: [5, 9, 15, 20]

    # Pop Items off stack
    print(stack.pop())  # print: 20

    print(stack.pop())  # print: 15

    print(stack.pop())  # print: 9

    print(stack.pop())  # print: 5

    print(stack.pop())  # Should raise an exception


if __name__=='__main__':
    main()