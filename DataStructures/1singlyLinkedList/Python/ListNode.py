class ListNode(object):

    def __init__(self, item=None, link=None):
        """
        Creates a ListNode with the specified data value and link
        :param item:
        :param link:
        """
        self.item = item
        self.link = link

    def get_item(self):
        """returns the data element stored as the node
        :return item:
        """
        return self.item

    def set_item(self, item=None):
        """sets the daa element stored at the node
        :param item:
        """
        self.item = item

    def get_link(self):
        """returns the next link stores at the node
        :return link:
        """
        return self.link

    def set_link(self, link=None):
        """returns the next link stored at the node
        :param link:
        """
        self.link = link


class LinkedList(object):

    def __init__(self, seq=[]):
        """creates a linked list"""
        self.head = None
        self.size = 0

        # if passed a sequence enter items to a list
        self.append([x for x in seq])

    def __len__(self):
        """returns number of items in the list
        :return size:
        """
        return self.size

    def _find(self, item):
        """private methods that returns node that is as the location in the lost
        :return node:
        :param item:
        """
        assert 0 <= item < self.size
        node = self.head

        # Move forward till we find the node
        for i in range(item):
            node = node.link

        return node

    def _delete(self, position):
        """private method to delete item at location from the list
        :param position:
        """
        if position == 0:
            # save item fron the initial node
            item = self.head.item

            # change head to point over the deleted node
            self.head = self.head.link
        else:
            # find previous node before deletion
            prev_node = self._find(position - 1)

            # save the item from node to delete
            item = prev_node.link.item

            # change predecessor to point over the deleted node
            prev_node.link = prev_node.link.item

        self.size -= 1
        return item


    def __getitem__(self, item):
        """returns data item at location item
        :return node.item:
        """
        node = self._find(item)
        return node.item

    def __setitem__(self, position, value):
        """set data at location position to value
        :param position:
        :param value:
        """
        node = self._find(position)
        node.item = value

    def __delitem__(self, position):
        """delete item at position from the list"""
        assert 0 <= position < self.size

        self._delete(position)



    def append(self, x):
        """appends x onto the end of the list
        :param x:
        """
        newNode = ListNode(x)

        # Link it to the end of the list
        if self.head is not None:
            node = self._find(self.size - 1)
            node.link = newNode
        else:
            # Empty list
            self.head = newNode

        self.size += 1


if __name__ == '__main__':
    a = LinkedList(seq=[1, 2, 3])
    print(a)

