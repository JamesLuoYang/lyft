from car import Car
from engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from model import calliope, glissade, rorschach, thovex, palindrome

class CarFactory(Car):

    def __init__(self, engine, battery):
        super().__init__(engine, battery)
        self.needs_service = False

    def create_calliope(self, current_date, last_service_date, current_milleage, last_service_milleage):
        self.engine = CapuletEngine(last_service_date, current_milleage, last_service_milleage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.needs_service = calliope.needs_service(self.engine, self.battery)
        return CarFactory(self.engine, self.battery)
    
    def create_thovex(self, current_date, last_service_date, current_milleage, last_service_milleage):
        self.engine = CapuletEngine(last_service_date, current_milleage, last_service_milleage)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.needs_service = thovex.needs_service(self.engine, self.battery)
        return CarFactory(self.engine, self.battery)
    
    def create_rorschach(self, current_date, last_service_date, current_milleage, last_service_milleage):
        self.engine = WilloughbyEngine(last_service_date, current_milleage, last_service_milleage)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.needs_service = rorschach.needs_service(self.engine, self.battery)
        return CarFactory(self.engine, self.battery)
    
    def create_glissade(self, current_date, last_service_date, current_milleage, last_service_milleage):
        self.engine = WilloughbyEngine(last_service_date, current_milleage, last_service_milleage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.needs_service = glissade.needs_service(self.engine, self.battery)
        return CarFactory(self.engine, self.battery)
    
    def create_palindrome(self, current_date, last_service_date, current_milleage, last_service_milleage):
        self.engine = SternmanEngine(last_service_date, current_milleage, last_service_milleage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.needs_service = palindrome.needs_service(self.engine, self.battery)
        return CarFactory(self.engine, self.battery)