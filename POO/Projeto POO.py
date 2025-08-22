class Circle:
    pi = 3.14
    def __init__(self, circle_radius: float) -> None:
        self.radius = circle_radius
    def getArea(self) -> float:
        return Circle.pi * self.radius ** 2
    
    def getCircunferencia(self) -> float:
        return Circle.pi * self.radius * 2

circle = Circle(circle_radius=5)
print(f"A área do círculo é: {circle.getArea()} ")
print(f"A Circunferência do círculo é: {circle.getCircunferencia()} ")