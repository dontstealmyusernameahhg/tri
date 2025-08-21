class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""
        num = self.number
        for val, sym in mapping:
            while num >= val:
                result += sym
                num -= val
        return result

# Example
n = RomanConverter(29)
print(n.to_roman()) # Output: XXIX