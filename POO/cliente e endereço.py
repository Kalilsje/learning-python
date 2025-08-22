class Address:
    def __init__(self, road, number) -> None:
        self.road = road
        self.number = number
    
    def get_road(self):
        return self.road
    
    def get_number(self):
        return self.number
    
    def set_road(self):
        self.road = new_road
    
    def set_number(self):
        self.number = new_number
    
    def see_address(self):
        return f"{self.road}, {self.number}"

class CLiente:
    def __init__(self, name:str, address: Address) -> None:
        self.name = name
        self.address = address

address = Address("Rua A", 1234)
iury = CLiente("Iury", address)
print(iury.address.see_address())