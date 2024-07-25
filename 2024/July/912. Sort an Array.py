from random import randint

def partition(arr, low, high):
    pivot = arr[randint(low, high)]
    left, right = low, high
    i = low

    while i <= right:
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] > pivot:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
        else:
            i += 1

    return left

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        quick_sort(nums, 0, len(nums) - 1)
        return nums
