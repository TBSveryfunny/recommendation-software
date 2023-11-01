import random

def quicksort(list, start=0, end=None):
  if end is None:
    end = len(list) - 1
  # this portion of list has been sorted
  if start >= end:
    return
  # select random element to be pivot
  piv_index = random.randint(start, end)
  piv_element = list[piv_index]
  # swap random element with last element in sub-lists
  list[end], list[piv_index] = list[piv_index], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  ltp = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < piv_element:
      # swap element to the right-most portion of lesser elements
      list[i], list[ltp] = list[ltp], list[i]
      # tally that we have one more lesser element
      ltp += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[ltp] = list[ltp], list[end]
  # recursively sort left and right sub-lists
  quicksort(list, start, ltp - 1)
  quicksort(list, ltp + 1, end)

# Modified binary search algorithm, built to return a sublist of elements that start with a certain index
def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  mid_idx = 0
  mid_val = None
  while left_pointer < right_pointer:
    # calculate the middle index using the two pointers
    mid_idx = (right_pointer + left_pointer) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return (mid_idx, [mid_val])
    if target < mid_val:
      # set the right_pointer to the correct value
      right_pointer = mid_idx
    if target > mid_val:
      # set the left_pointer to the correct value
      left_pointer = mid_idx + 1

  # even and edge-case index correction
  list_end = len(sorted_list) - 1
  if not mid_val.startswith(target):
    if mid_idx == list_end:
      return (None, [])
    mid_idx += 1
    mid_val = sorted_list[mid_idx]
    if not mid_val.startswith(target):
      return (None, [])
  if mid_idx == list_end:
    return (mid_idx, [mid_val])
  
  # get remaining values that start with the target
  end_idx = mid_idx + 1
  while sorted_list[end_idx].startswith(target):
    end_idx += 1
  return (mid_idx, sorted_list[mid_idx:end_idx])