class A:
    def __init__(self) -> None:
        self.x = 0
    def increase(self, n):
        self.x += n
        print("self.x:", self.x)

a = A()
a.increase(1)
a.increase(1)
a.increase(2)
a.increase(1)
