#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code heredef selection_sort(arr):
        n = len(arr)
        for i in range(n):
            # Find the minimum element in the remaining unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # Swap the found minimum element with the first element of the unsorted part
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
