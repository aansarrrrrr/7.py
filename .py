class IterableWithGenerators:
  def __init__(self, n):
      self.n = n

  def __iter__(self):
      for i in range(self.n):

          yield self.generator(i)

  def generator(self, start):
      
      for i in range(start, start + 3):
          yield i


iterable = IterableWithGenerators(5)
for gen in iterable:
  for value in gen:
      print(value)
