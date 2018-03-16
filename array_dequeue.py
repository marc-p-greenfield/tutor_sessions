from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__front = 0


  def __str__(self):
      value = []
      if self.__size == 0:
          return "[ ]"
      for i in self.__contents:
          if i != None:
              value.append(i)
      result = "[ "
      for i in value[:len(value)-1]:
          result += str(i) + ", "

      result += str(value[len(value)-1])
      result += " ]"
      return result


  def __len__(self):
      return self.__size



  def __grow(self):
      old_array = self.__contents
      self.__contents = [None] * self.__capacity * 2
      for k in range(self.__size):
          self.__contents[k] = old_array[self.__front]
          self.__front = (1 + self.__front) % len(old_array)
      self.__front = 0
      self.__capacity = self.__capacity * 2



  def push_front(self, val):
      if self.__size == self.__capacity:
          self.__grow()
      pos = (self.__front + 1) % len(self.__contents)
      self.__contents[pos] = val
      self.__front = pos
      self.__size +=1

  def pop_front(self):
      remove = self.__contents[self.__front]
      self.__contents[self.__front] = None
      self.__front = (self.__front + 1) % len(self.__contents)
      self.__size -= 1


  def peek_front(self):
      peek_front = self.__contents[self.__front]
      return peek_front


  def push_back(self, val):
      if self.__size == self.__capacity:
          self.__grow()
      pos = (self.__front + self.__size) % len(self.__contents)
      self.__contents[pos] = val
      self.__size += 1
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.


  def pop_back(self):
      back = (self.__front + self.__size - 1) % len(self.__contents)
      remove = self.__contents[back]
      self.__contents[back] = None
      self.__size -= 1

  def peek_back(self):
      back = (self.__front + self.__size - 1) % len(self.__contents)
      peek_back = self.__contents[back]
      return peek_back

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
a = Array_Deque()
a.push_front(9)
a.push_back(10)
print (a)
a.push_front(11)
print(a)
