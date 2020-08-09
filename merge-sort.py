def mergeSort(arr):
	N = len(arr)
	if N <= 1:
		return

	mid = N//2
	L = arr[:mid]
	R = arr[mid:]

	mergeSort(arr)
	mergeSort(arr)

	i = j = k = 0

	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = L[j]
			j += 1

		k += 1

	while i < len(L):
		arr[k] = L[i]
		i += 1
		k += 1

	while j < len(R):
		arr[k] = R[j]
		j += 1
		k += 1