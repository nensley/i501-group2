import unittest
import pandas as pd
from preprocess_input import preprocess_input_data

# To run the unit test: python -m unittest preprocess_test

# defines a class to test potential edge cases and parameter values
class TestPreprocessInputData(unittest.TestCase):

    def test_valid_input(self):
        # Test a valid input case
        result = preprocess_input_data(17, "Male", "Professional School", "Executive/Management", "Other", 40)
        expected_columns = ['age-group', 'sex', 'education-yr', 'occupation', 'employment-type', 'race']
        # Check whether result columns match expected
        self.assertEqual(list(result.columns), expected_columns)

        # Check that the education-yr is correctly mapped
        self.assertEqual(result['education-yr'].iloc[0], 22)

        # Check that the occupation is mapped correctly
        self.assertEqual(result['occupation'].iloc[0], "Exec-managerial")

        # Check that employment-type is categorized correctly
        self.assertEqual(result['employment-type'].iloc[0], 'full_time')

        # Check that age-group is categorized correctly
        self.assertEqual(result['age-group'].iloc[0], '17-34')

    def test_edge_case_age(self):
        # Test edge case where age is exactly 35
        result = preprocess_input_data(35, "Male", "Bachelors", "Sales", "Asian", 30)
        self.assertEqual(result['age-group'].iloc[0], '35+')

    def test_race_mapping(self):
        # Test race mapping to see if it maps correctly or keeps original if not mapped
        result = preprocess_input_data(30, "Female", "Some College", "Tech-support", "Asian or Pacific Islander", 40)
        self.assertEqual(result['race'].iloc[0], "Asian-Pac-Islander")

    # These functions test employment classifications along the edge
    def test_part_time_employment(self):
        # Test for part-time employment
        result = preprocess_input_data(34, "Female", "HS Grad", "Sales", "Black", 20)
        self.assertEqual(result['employment-type'].iloc[0], 'part_time')

    def test_full_time_employment(self):
        # Test for full-time employment
        result = preprocess_input_data(35, "Male", "Bachelors", "Exec-managerial", "White", 40)
        self.assertEqual(result['employment-type'].iloc[0], 'full_time')

    def test_overtime_employment(self):
        # Test for overtime employment
        result = preprocess_input_data(41, "Female", "Masters", "Prof-specialty", "Asian", 50)
        self.assertEqual(result['employment-type'].iloc[0], 'over_time')

if __name__ == '__main__':
    unittest.main()