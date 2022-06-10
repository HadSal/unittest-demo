from unittest import TestCase
from unittest.mock import Mock

from optimisation_algorithm import OptimisationAlgorithm, optimise_appointments


class TestOptimisationAlgorithm(TestCase):
    def test_optimise(self):
        # GIVEN
        api = Mock()
        api.get_appointments = Mock(return_value=["b", "c", "a"])
        algorithm = OptimisationAlgorithm(api)
        expected = ["a", "b", "c"]

        # WHEN
        data = algorithm.optimise()

        # THEN
        self.assertEqual(data, expected)

    def test_load_data_fail(self):
        # GIVEN
        api = Mock()
        api.get_appointments = Mock(return_value=["b", "c", "bad_appointment"])
        algorithm = OptimisationAlgorithm(api)

        # WHEN
        call = algorithm.load_data

        # THEN
        self.assertRaises(ValueError, call)

    def test_optimise_appointments(self):
        subtests = [
            (["b", "c", "a"], ["a", "b", "c"], "Three elements"),
            (["a", "a"], ["a", "a"], "Two elements"),
        ]

        for appointments, expected, subtest_description in subtests:
            optimised = optimise_appointments(appointments)
            with self.subTest(msg=subtest_description, obtained=optimised, expected=expected):
                self.assertEqual(optimised, expected)
