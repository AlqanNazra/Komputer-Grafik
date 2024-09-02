"""
class bentuk:
    pass
"""

"""
class bentuk:
    def __init__(self, x, y):
        self.x_awal = x
        self.y_awal = y
"""


class bentuk:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def persegi(self, sisi):
        return f"persegi titik awal {self.x} {self.x} dan sisi {sisi}"

karya1 = bentuk(80,80)
print(karya1.persegi(80))