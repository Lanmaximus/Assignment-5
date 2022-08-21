class Ans:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def answer(self):
        return self.x**self.y
a = Ans(10,3)
print(a.answer())