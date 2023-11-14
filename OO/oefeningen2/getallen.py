class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def adder(self):
        return self.a + self.b

    def subtract(self):
        return self.a-self.b


x = Numbers(9,6)
print(x.adder(), x.subtract(),x.multiply(), x.divide())