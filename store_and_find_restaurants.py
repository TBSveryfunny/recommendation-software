from restaurantData import types
from sort_and_search_types import binary_search

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  # modified insertion scheme to ensure that the list of restaurants is in order of the overall quality, highest to lowest.
  # This is in line with how real recommendation systems should behave.
  def insert_sorted(self, new_node):
    if self.head_node == None:
      new_node.set_next_node(self.head_node)
      self.head_node = new_node
    elif self.head_node.value[1].total_score <= new_node.value[1].total_score:
      new_node.set_next_node(self.head_node)
      self.head_node = new_node
    else:
      current_node = self.head_node
      while(current_node.get_next_node() != None and current_node.get_next_node().value[1].total_score > new_node.value[1].total_score):
        current_node = current_node.get_next_node()
      new_node.set_next_node(current_node.get_next_node())
      current_node.set_next_node(new_node)

  # string representation of list for final product
  def __str__(self):
    st = ""
    current_node = self.head_node
    while(current_node):
      st += "\n\n----------------------------\n\n"
      st += current_node.get_value()[1].__str__()
      current_node = current_node.get_next_node()
    return st

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]

  # custom hash function. Due to the 0(log n) runtime of binary search, a
  # is-number check is implemented to add the option of simply using the key 
  # from when the function is called from the main loop instead.
  def hash(self, key):
    if type(key) == int:
      return key
    else:
      return binary_search(types, key)[0]

  def compress(self, hash_code):
    return hash_code % self.array_size

  # Anti-collision method omitted due to the custom hash function and the use of linked lists as the return value.
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    return list_at_array
  
  def assign(self, key, value):
    payload = Node([key, value])
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    list_at_array.insert_sorted(payload)