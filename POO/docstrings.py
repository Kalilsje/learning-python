class A:
    def __init__(self) -> None:
        self.attr1 = None
        self.attr2 = None
    def get_attr1(self):
        return self.attr1
print(help(A))