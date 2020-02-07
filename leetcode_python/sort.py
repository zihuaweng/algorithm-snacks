#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


#!/usr/bin/env python3
# coding: utf-8

from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def func_wrapper(cls, *args):
        start = time.monotonic_ns()
        arr = func(cls, *args)
        print(time.monotonic_ns() - start)
        return arr

    return func_wrapper


class SelectionSort:
    # @time_it
    def sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            # Replace the arr.
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


class InsertionSort:
    # @time_it
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            # Switch the element to the right when the last element is smaller.
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr


class HeapSort:
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # compare left child to the parent
        if l < n and arr[l] > arr[i]:
            largest = l

        # compare the right to the largest as the largest might change previously.
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]

            # Only run recursively when largest changed.
            self.heapify(arr, n, largest)

    # @time_it
    def sort(self, arr):
        # First build the maxheap, start from bottom every time (bottom-up)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            self.heapify(arr, n, i)

        # Retrieve the largest element and swap with the last element each time
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            # Only need to check 0 as 0 is the only one changed
            self.heapify(arr, i, 0)

        return arr


class MergeSort:
    def merge(self, arr, arr_l, arr_r):
        # Copy sort element to arr
        i = l = r = 0
        while l < len(arr_l) and r < len(arr_r):
            if arr_l[l] < arr_r[r]:
                arr[i] = arr_l[l]
                l += 1
            else:
                arr[i] = arr_r[r]
                r += 1
            i += 1

        # check if any elements left
        if l < len(arr_l):
            arr[i:] = arr_l[l:]
        if r < len(arr_r):
            arr[i:] = arr_r[r:]
        return arr

    def merget_sort(self, arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2

        return self.merge(arr, self.merget_sort(arr[:mid]), self.merget_sort(arr[mid:]))

    # @time_it
    def sort(self, arr):
        return self.merget_sort(arr)


class QuickSort:
    def quick_sort(self, arr, left, right):
        if right <= left:
            return
        start = left
        end = right
        p = right
        while left < right:
            # First check elements that already smaller than pivot (l) and
            # larger than pivot (r). Swap them when needed.
            while left < right:
                while arr[left] < arr[p] and left < right:
                    left += 1
                while arr[right] >= arr[p] and left < right:
                    right -= 1
                if left != right:
                    arr[left], arr[right] = arr[right], arr[left]
            arr[right], arr[p] = arr[p], arr[right]
        self.quick_sort(arr, start, right - 1)
        self.quick_sort(arr, right + 1, end)

    # @time_it
    def sort(self, arr):
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr


def test():
    arr_text = [12, 11, 13, 5, 6, 1, 3, 2, 9]
    print(SelectionSort().sort(arr_text))
    arr_text = [12, 11, 13, 5, 6, 1, 3, 2, 9]
    print(InsertionSort().sort(arr_text))
    arr_text = [12, 11, 13, 5, 6, 1, 3, 2, 9]
    print(HeapSort().sort(arr_text))
    arr_text = [12, 11, 13, 5, 6, 1, 3, 2, 9]
    print(MergeSort().sort(arr_text))
    arr_text = [12, 11, 13, 5, 6, 1, 3, 2, 9]
    print(QuickSort().sort(arr_text))


if __name__ == '__main__':
    test()
