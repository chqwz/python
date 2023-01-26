import random

class Marm():
    """описание мармеладки"""
    def __init__(self, color, form):
        self.color = color
        self.form = form
        
    def selected(self):
        print("Ваша мармеладка " + self.color + " цвета и " + self.form + " формы.")
        
c = ["красного", "жёлтого", "зеленого", "голубого", "радужного", "фиолетового"]
f = ["квадратной", "круглой", "мишковидной", "червечковидной"]

a = c[random.randint(0, 5)]
b = f[random.randint(0, 3)]
        
marm1 = Marm(a, b)

marm1.selected()