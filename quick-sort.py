def partition(arr, l, h):
  p = s

  while l < h:
    while l <= h and arr[l] <= arr[p]:
      l += 1

    while l <= h and arr[p] < arr[h]:
      h -= 1

    if l < h:
      arr[l], arr[h] = arr[h], arr[l]

  arr[p], arr[h] = arr[h], arr[p]
  return h

def quicksort(arr, s, e):
  if s < e:
    mid = partition(arr, s, e)
    quicksort(arr, s, mid-1)
    quicksort(arr, mid+1, e)
