from optimisation_api import OptimisationAPI


class OptimisationAlgorithm:

    def __init__(self, api: OptimisationAPI):
        self.api = api  # hoisting the api to the constructor is essential for unit testing

    def optimise(self):
        appointments = self.load_data()
        return optimise_appointments(appointments)

    def load_data(self):
        appointments = self.api.get_appointments()
        if "bad_appointment" in appointments:
            raise ValueError("Bad appointment !")
        return appointments


def optimise_appointments(appointments):
    return sorted(appointments)
