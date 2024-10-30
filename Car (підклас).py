class Car(Vehicle): # type: ignore
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels

    def drive(self):
        print(f"{self.name} їде {self.wheels} на колесах.")
