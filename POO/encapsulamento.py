class CLients:
    def __init__(self) -> None:
        self.data = []
    
    def add_client(self, client):
        self.data.append(client)
    
    def get_client(self):
        return self.data
    
    def remove_client(self, client):
        if client in self.data:
            self.data.remove(client)
            return True
        else:
            return False
        
clients_data = CLients()

# Getter
@property
def data(self):
    return self._data

# Setter
@data.setter
def data(self, value):
    if isinstance(value, list):
        self._data = value
    else:
        print("Valor Invalido")
