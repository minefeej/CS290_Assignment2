# Course: CS261 - Data Structures
# Student Name: Joseph Minefee
# Assignment: Assignment 2: Implementation of Dynamic Array and ADTs using Dynamic Array and Amortized Analysis
# Description:  Implement a Dynamic Array, a Bag ADT, a Stack ADT, and a Queue ADT.
# Last revised: 1/29/21


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # ------------------------------------------------------------------ #

    def resize(self, new_capacity: int) -> None:
        """
        Resizes the underlying static array to the new capacity.
        """
        # Checking if passed capacity is positive and greater than the size of the dynamic array. Then creates a new
        # Static array using the new capacity and copies the old data to the new array.
        if new_capacity > 0 and new_capacity >= self.size:
            new_arr = StaticArray(new_capacity)
            for index in range(self.size):
                new_arr[index] = self.data[index]
            self.data = new_arr
            self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Appends a value to the end of the dynamic array.
        """
        # When the size is equal to the capacity, the capacity is increased and then the values are appended.
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a passed value at a specified index and moves the existing elements to fit the inserted value.
        """
        # Checks if the index is out of bound and raises exception.
        if index < 0 or index > self.size:
            raise DynamicArrayException('Index out of bounds')
        # Checks if the capacity needs to be increased and calls resize if it does.
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        # Moves values in array to make room for new value at the passed index.
        for ind in range(self.size - 1, index - 1, -1):
            self.data[ind + 1] = self.data[ind]
        # Populates new value in the array at the specified index and increments size.
        self.data[index] = value
        self.size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Removes element from array at passed index and resizes if needed.
        """
        # Checks if the index is out of bound and raises exception.
        if index < 0 or index >= self.size:
            raise DynamicArrayException('Index out of bounds')
        # Checks if array is empty and raises an exception.
        if self.size == 0:
            raise DynamicArrayException('Array is empty')
        # Checks if capacity needs to be reduced. If size is 1/4 of capacity it reduces the capacity.
        if self.size < (self.capacity / 4):
            # If capacity is greater than 10 but double the size is less than 10, a new array is created of capacity 10.
            if self.capacity > 10:
                if (self.size * 2) < 10:
                    new_arr = StaticArray(10)
                    for ind in range(self.size):
                        new_arr[ind] = self.data[ind]
                    self.data = new_arr
                    self.capacity = 10
                # Else a new array is created twice the size of the array.
                else:
                    new_arr = StaticArray(self.size * 2)
                    for ind in range(self.size):
                        new_arr[ind] = self.data[ind]
                    self.data = new_arr
                    self.capacity = self.size * 2
        # Removing the element at the index and filling in the gaps.
        for ind in range(index, self.size - 1):
            self.data[ind] = self.data[ind + 1]
        # Reduces size by one.
        self.size -= 1

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new Dynamic Array object that contains the requested number of elements from the original array
        starting with the element located at the requested start index.
        """
        # Checks if the index is out of bound and raises exception.
        if start_index < 0 or start_index + size > self.size or size < 0:
            raise DynamicArrayException('Index out of bounds or size is too great')
        # Creates a new array
        new_arr = DynamicArray()
        new_arr.size = 0
        count = 0
        # Loops through original array and sets values into the new array.
        for index in range(start_index, start_index + size):
            new_arr.size += 1
            if new_arr.size == new_arr.capacity:
                new_arr.resize(2 * new_arr.capacity)
            new_arr[count] = self.data[index]
            count += 1
        # Returns new array.
        return new_arr

    def merge(self, second_da: object) -> None:
        """
        Appends all elements from another array in the same order as they are stored in the second array.
        """
        # Loops through elements in second_da and appends to the original array object.
        for index in range(second_da.size):
            self.append(second_da[index])


    def map(self, map_func) -> object:
        """
        TODO: Write this implementation
        """
        pass

    def filter(self, filter_func) -> object:
        """
        TODO: Write this implementation
        """
        pass

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        TODO: Write this implementation
        """
        pass





# BASIC TESTING
if __name__ == "__main__":


    # print("\n# resize - example 1")
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.resize(8)
    # print(da.size, da.capacity, da.data)
    # da.resize(2)
    # print(da.size, da.capacity, da.data)
    # da.resize(0)
    # print(da.size, da.capacity, da.data)
    #
    #
    # print("\n# resize - example 2")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)
    #
    # print("\n# resize - example 3")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(948)
    # print(da)
    # da.resize(8)
    # print(da)
    #
    #
    # print("\n# append - example 1")
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.append(1)
    # print(da.size, da.capacity, da.data)
    # print(da)
    #
    #
    # print("\n# append - example 2")
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)
    #
    #
    # print("\n# append - example 3")
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.size)
    # print(da.capacity)
    #
    #
    # print("\n# insert_at_index - example 1")
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)
    #
    #
    # print("\n# insert_at_index example 2")
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)
    #
    # print("\n# insert at index example 3")
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Cannot insert value", value, "at index", index)
    # print(da)
    #
    #
    # print("\n# remove_at_index - example 1")
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # print(da)
    # da.remove_at_index(6)
    # print(da)
    # da.remove_at_index(2)
    # print(da)
    #
    #
    # print("\n# remove_at_index - example 2")
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    # print(da.size, da.capacity)
    # for i in range(16, -1, -1):
    #     da.remove_at_index(0)
    # print(da)
    #
    #
    # print("\n# remove_at_index - example 3")
    # da = DynamicArray()
    # print(da.size, da.capacity)
    # [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)  # step 3 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)  # step 4 - remove 1 element
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)  # step 6 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)  # step 7 - remove 1 element
    # print(da.size, da.capacity)
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.size, da.capacity, end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.size, da.capacity)
    #
    #
    # print("\n# remove at index - example 4")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # print(da)
    # for _ in range(5):
    #     da.remove_at_index(0)
    #     print(da)
    #
    # print("\n# remove at index - example 5")
    # da = DynamicArray([1204, -45242, -11974, 50207, 99370])
    # try:
    #     da.remove_at_index(5)
    # except Exception as e:
    #     print("Exeptions raised:", type(e))
    # print(da)
    #
    #
    # print("\n# slice example 1")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")
    #
    #
    # print("\n# slice example 2")
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", da)
    # da_slice = da.slice(0, 5)
    # print(da_slice)
    # print(da_slice.data)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")
    #
    #
    # print("\n# merge example 1")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)
    #
    #
    # print("\n# merge example 2")
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)
    #
    #
    # print("\n# map example 1")
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # print(da.map(lambda x: x ** 2))
    #
    # print("\n# map example 2")
    #
    #
    # def double(value):
    #     return value * 2
    #
    # def square(value):
    #     return value ** 2
    #
    # def cube(value):
    #     return value ** 3
    #
    # def plus_one(value):
    #     return value + 1
    #
    # da = DynamicArray([plus_one, double, square, cube])
    # for value in [1, 10, 20]:
    #     print(da.map(lambda x: x(value)))
    #
    #
    # print("\n# filter example 1")
    # def filter_a(e):
    #     return e > 10
    #
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # result = da.filter(filter_a)
    # print(result)
    # print(da.filter(lambda x: (10 <= x <= 20)))
    #
    #
    # print("\n# filter example 2")
    # def is_long_word(word, length):
    #     return len(word) > length
    #
    # da = DynamicArray("This is a sentence with some long words".split())
    # print(da)
    # for length in [3, 4, 7]:
    #     print(da.filter(lambda word: is_long_word(word, length)))
    #
    #
    # print("\n# reduce example 1")
    # values = [100, 5, 10, 15, 20, 25]
    # da = DynamicArray(values)
    # print(da)
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    #
    #
    # print("\n# reduce example 2")
    # da = DynamicArray([100])
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    # da.remove_at_index(0)
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))