"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
	low = 0
	high = len(array) -1
	array = quicksort2(array,low,high)
	return array



def quicksort2(array,low , high):
	
	if low < high:
		pivotpos = get_pivot(array, low, high)
		quicksort2(array, low, pivotpos-1)
		quicksort2(array, pivotpos+1, high)
	return array
	

def get_pivot(array, low , high):
	pivot = array[low]
	# low = 0
	# high = len(array) -1
	while low < high:
		while low < high and array[high]>= pivot:
			high -= 1
		array[low] = array[high]
		while low < high and array[low] <= pivot:
			low += 1
		array[high] = array[low]
	array[low] = pivot
	return low


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
