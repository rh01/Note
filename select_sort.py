def select_sort(A):
	for i in range(0, len(A) - 1):
		min_index = i
		for j in range(i+1, len(A)):
			if A[j] < A[min_index]:
				min_index = j
		if min_index != i:
			A[i], A[min_index] = A[min_index], A[i]

	return A

print select_sort([2,3,2,6,9,0])

