class Counter:
  """Creates a counter that counts how many times something has happened."""
  def __init__(self):
    self.count = 0

  def count(self) -> int:
    """
    Returns:
        int: amount of times that something happened
    """
    return self.count

  def add_counter(self, value: int = 1):
    """Increase the counter.

    Args:
        value (int, optional): The value to increase the counter. Defaults to 1.
    """
    self.count += value

counter = Counter()

travel_counter = Counter()
