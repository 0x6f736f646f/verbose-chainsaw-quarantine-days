class Stack(object):

    def __init__(self):
        """creates and empty LIFO stack"""
        self.item = []

    def push(self, item):
        """places x on top of the stack
        :param item
        """
        self.item.append(item)

    def pop(self):
        """removes and returns the top element of the stack
        :return item
        """
        if self.size() > 0:
            return self.item.pop()
        else:
            return IndexError

    def top(self):
        """show the top element of the stack without removing it
        :returns item
        """
        if self.size() > 0:
            return self.item[-1]
        else:
            return IndexError

    def size(self):
        """returns the number of elements in the stack
        :return size
        """
        return len(self.item)