class Restaurant:

  def __init__(self, data):
    self.name = data[0]
    self.price = data[1]
    self.rating = data[2]
    self.address = data[3]
    self.total_score = int(self.price) + int(self.rating)

  def __str__(self):
    return f"Name: {self.name}\nPrice: {self.price}/5\nRating: {self.rating}/5\nAddress: {self.address}"