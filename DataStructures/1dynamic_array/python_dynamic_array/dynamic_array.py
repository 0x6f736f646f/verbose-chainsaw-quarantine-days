import ctypes
import sys


class DynamicArray:
    def __init__(self):
        self.n = 0
        self._capacity = 1
        self._A = self.make_array(self._capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            raise IndexError("Ivalid index")
        return self._A[item]

    def append(self, item):
        if self.n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self.n] = item
        self.n += 1

    def _resize(self, c):
        B = self.make_array(c)
        for k in range(self.n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    @staticmethod
    def make_array(c):
        return (c * ctypes.py_object)()

    @property
    def a(self):
        return self._A


def main():
    dynamic_array = DynamicArray()
    for k in range(10):
        dynamic_array.append(k)
        a = dynamic_array.__len__()
        b = sys.getsizeof(dynamic_array.a)
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))


if __name__ == '__main__':
    main()
