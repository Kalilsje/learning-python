class A:
    def __init__(self) -> None:
        self.attr1 = 1
        self.attr2 = "kalil"
    def method1(self):
        return self.attr1

a_obj = A()
for item in a_obj.__dict__.keys():
    print(item)