class AmphibiousVehicle(Car, Boat): # type: ignore
    def __init__(self, name, wheels, capacity):
        Car.__init__(self, name, wheels) # type: ignore
        Boat.__init__(self, name, capacity) # type: ignore

    def drive_and_sail(self):
        self.drive()
        self.sail()
