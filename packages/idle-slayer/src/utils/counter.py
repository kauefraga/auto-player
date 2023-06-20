class Counter:
  def __init__(self):
    self.count = 0

  def count(self) -> int:
    return self.count

  def add_counter(self):
    self.count += 1

counter = Counter()
