# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:

from dynamic_array import DynamicArray

class Bag:
    def __init__(self, start_bag=None):
        self._da = DynamicArray()
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_)) for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        return self._da.length()

    def add(self, value: object) -> None:
        self._da.append(value)

    def remove(self, value: object) -> bool:
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        if self.size() != second_bag.size():
            return False
        first_bag_dict = {}
        second_bag_dict = {}
        for i in range(self._da.length()):
            value = self._da.get_at_index(i)
            if value in first_bag_dict:
                first_bag_dict[value] += 1
            else:
                first_bag_dict[value] = 1
        for i in range(second_bag.size()):
            value = second_bag._da.get_at_index(i)
            if value in second_bag_dict:
                second_bag_dict[value] += 1
            else:
                second_bag_dict[value] = 1
        return first_bag_dict == second_bag_dict

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self._da.length():
            value = self._da.get_at_index(self._index)
            self._index += 1
            return value
        else:
            raise StopIteration

