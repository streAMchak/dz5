class Boat(Vehicle): # type: ignore
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def sail(self):
        print(f"{self.name} пливе з місткістю {self.capacity} людей.")
