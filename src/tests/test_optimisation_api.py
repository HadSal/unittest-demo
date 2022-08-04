from unittest import TestCase

from optimisation_api import OptimisationAPI


class TestOptimisationAPI(TestCase):
    def test_add_appointment(self):
        # GIVEN
        api = OptimisationAPI()
        list1 = ["a"]
        appointment = "b"
        expected = ["a", "b"]

        # WHEN
        result = api.add_appointment(list1, appointment)

        # THEN
        self.assertEqual(result, expected)
