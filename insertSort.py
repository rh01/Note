def insert_sort(A):
	list_len = len(A)
	if list_len < 2:
		return A
	for i in range(1, list_len):
		cursor = A[i]
		for j in range(i-1,0,-1):
			if A[j] > cursor:
				A[j + 1] =  A[j]
			
			else:
				A[j + 1] = cursor
				break
	return A

print insert_sort([3,4,6,5,8,3,9,0,1])

