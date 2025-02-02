import numpy as np

class ShipParams():
    fuel: np.ndarray    #  (kg)
    power: np.ndarray   #  (W)
    rpm: np.ndarray     #  (Hz)
    speed: np.ndarray   #  (m/s)
    fuel_type: str

    def __init__(self, fuel, power, rpm, speed):
        self.fuel = fuel
        self.power = power
        self.rpm = rpm
        self.speed = speed
        self.fuel_type = 'HFO'

    @classmethod
    def set_default_array(cls):
        return cls(
            speed = np.array([[0]]),
            fuel = np.array([[0]]),
            power = np.array([[0]]),
            rpm = np.array([[0]])
        )

    def print(self):
        print('fuel: ', self.fuel)
        print('rpm: ', self.rpm)
        print('power: ', self.power)
        print('speed: ', self.speed)
        print('fuel_type: ', self.fuel_type)

    def print_shape(self):
        print('fuel: ', self.fuel.shape)
        print('rpm: ', self.rpm.shape)
        print('power: ', self.power.shape)
        print('speed: ', self.speed.shape)

    def define_variants(self, variant_segments):
        self.speed = np.repeat(self.speed, variant_segments + 1, axis=1)
        self.fuel = np.repeat(self.fuel, variant_segments + 1, axis=1)
        self.power = np.repeat(self.power, variant_segments + 1, axis=1)
        self.rpm = np.repeat(self.rpm, variant_segments + 1, axis=1)

    def get_power(self):
        return self.power

    def get_fuel(self):
        return self.fuel

    def get_full_fuel(self):
        fuel = np.sum(self.fuel)
        return fuel

    def get_fuel_type(self):
        return self.fuel_type

    def get_rpm(self):
        return self.rpm

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        self.speed = new_speed

    def set_fuel(self, new_fuel):
        self.fuel = new_fuel

    def set_rpm(self, new_rpm):
        self.rpm = new_rpm

    def set_power(self, new_power):
        self.power = new_power

    def select(self, idxs):
        self.speed = self.speed[:, idxs]
        self.fuel = self.fuel[:, idxs]
        self.power = self.power[:, idxs]
        self.rpm = self.rpm[:, idxs]

    def flip(self):
        self.speed=np.flip(self.speed,0)
        self.fuel = np.flip(self.fuel,0)
        self.power = np.flip(self.power,0)
        self.rpm = np.flip(self.rpm,0)