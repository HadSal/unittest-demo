import uuid
import random


class OptimisationAPI:

    def __init__(self, rnd=random.Random()):
        self.rnd = rnd
        self.appointments = [self.generate_appointment() for _ in range(10)]

    def generate_appointment(self):
        return uuid.UUID(int=self.rnd.getrandbits(128))

    def get_appointments(self):
        return self.appointments

    def add_appointment(self, list1, appointment):
        list1.append(appointment)
        return list1

    def delete_appointment(self):
        pass
