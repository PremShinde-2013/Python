class Temperature:
    def __init__(self, celsius):
        self.celsius = float(celsius)           # instance data

    def to_f(self):                        # instance method (uses self)
        return (self.celsius * 9/5) + 32

    @classmethod
    def from_fahrenheit(cls, f):           # class method (builds objects)
        celsius = (f - 32) * 5/9
        return cls(celsius)                      # uses cls, not a hard-coded name

    @staticmethod
    def is_freezing_c(celsius):                  # static method (utility)
        return celsius <= 0

t = Temperature(25)
print(t.to_f())                            # 77.0
t2 = Temperature.from_fahrenheit(77)
print(t2.celsius)                                # 25.0
print(Temperature.is_freezing_c(-5))       # True
