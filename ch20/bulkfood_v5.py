import model_v5 as model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


try:
    truffle = LineItem('White truffle', 100, 0)
except ValueError as exc:
    print('ValueError: {}'.format(exc))

try:
    truffle = LineItem(' ', 300, 20.12)
except ValueError as exc:
    print('ValueError: {}'.format(exc))

