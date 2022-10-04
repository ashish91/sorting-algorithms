def merge(arr, low, mid, high):
  N = mid + 1 - low
  M = high - mid

  aux = [None]*(N+M)

  i, j, k = low, mid+1, 0
  while i < N and j < M:
    if arr[i] <= arr[j]:
      aux[k] = arr[i]
      i += 1
    else:
      aux[k] = arr[j]
      j += 1
    k += 1

  while i < N:
    aux[k] = arr[i]
    i += 1
    k += 1

  while j < M:
    aux[k] = arr[j]
    j += 1
    k += 1

  # Copy elements back to arr from aux
  for i in range(N+M):
    arr[i+low] = aux[i]

def mergesort(arr, s, e):
  if s < e:
    mid = s + (e-s)//2
    mergesort(arr, s, mid)
    mergesort(arr, mid+1, e)
    merge(arr, s, mid, e)
