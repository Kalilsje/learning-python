class Ventilador:
    model = "ABC"
    def _init_(self, velocity = 0, state = False, rotation = False) -> None:
        self.state = state
        self.velocity = velocity
        self.rotation = rotation
    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def change_velocity(self, velocity):
        self.velocity = velocity
    
    def turn_on_rotation(self, velocity):
        self.rotation = True
    
    def turn_on_rotation(self):
        self.rotation = True
    
    def turn_off_rotation(self):
        self.rotation = False
Ventilador_1 = Ventilador()
Ventilador_1.turn_on()
print(Ventilador_1.state)

Ventilador_1.change_velocity(20)
print(Ventilador_1.velocity)

Ventilador_1.turn_on_rotation()
print(Ventilador_1.rotation)

ventilador_2 = Ventilador()
print(Ventilador_1.model)
print(Ventilador_2.model)
print(Ventilador.model)

@classmethod
def change_model(cls, new_model):
    cls.model = new_model

@classmethod
def see_model(cls):
    return cls.model

@staticmethod
def pick_tax_velocity():
    tax 0.1
    return tax 