import unittest
import requests

class TestPostRequests(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:8000/get_form/"

    def send_post_request(self, form_data):
        response = requests.post(self.url, data=form_data)
        return response.text

    def test_valid_data_1(self):
        #Test for find form with 4 real fields and with date type DD.MM.YYYY
        form_data = {'f_name': 'John', 'f_email': 'john@example.com', 'f_phone': '+71234567890', 'f_date': '24.07.2023'}
        response = self.send_post_request(form_data)
        self.assertIn('MyForm_1_NEPD', response)

    def test_valid_data_2(self):
        #Test for find form with 3 real fields and 1 field not in the form
        form_data = {'f_name': 'John', 'f_email': 'john@example.com', 'f_phone': '+71234567890', 'f_date': '24.07.2023', 'sometext': 'TEXTFORTEXT'}
        response = self.send_post_request(form_data)
        self.assertIn('MyForm_1_NEPD', response)

    def test_valid_data_3(self):
        #Test for find form with 3 real fields
        form_data = {'f_name': 'John', 'f_email': 'john@example.com', 'f_phone': '+71234567890'}
        response = self.send_post_request(form_data)
        self.assertIn('MyForm_2_NEP', response)
    
    def test_valid_data_4(self):
        #Test for find form with 2 real fields
        form_data = {'f_name': 'John', 'f_email': 'john@example.com'}
        response = self.send_post_request(form_data)
        self.assertIn('MyForm_3_NE', response)
    
    def test_valid_data_5(self):
        #Test for find form with 1 real field
        form_data = {'f_name': 'John'}
        response = self.send_post_request(form_data)
        self.assertIn('MyForm_4_N', response)
    
    def test_valid_data_6(self):
        #Test checked 1 real field in form and 4 fields which are not in the form
        form_data = {'f_name': 'John', 'my_email': 'john@example.com', 'my_phone': '+71234567890', 'my_date': '24.07.2023', 'sometext': 'TEXTFORTEXT'}
        response = self.send_post_request(form_data)
        self.assertIn('MyForm_4_N', response)

    def test_valid_data_7(self):
        #Test for another type of date YYYY-MM-DD
        form_data = {'f_name': 'John', 'f_email': 'john@example.com', 'f_phone': '+71234567890', 'f_date': '2023-07-24'}
        response = self.send_post_request(form_data)
        self.assertIn('MyForm_1_NEPD', response)

    def test_invalid_data_1(self):
        #Test for check correctly validate types and get correctly
        form_data = {'f_name': '+71234567890', 'f_email': 'invalid', 'f_phone': '123', 'f_date': 'invalid_date'}
        response = self.send_post_request(form_data)
        self.assertIn('{"f_name": "TYPE_PHONE", "f_email": "TYPE_TEXT", "f_phone": "TYPE_TEXT", "f_date": "TYPE_TEXT"}', response)

    def test_invalid_data_2(self):
        #Test for check correctly validate types and get correctly
        form_data = {'name': 'John', 'email': 'jhon@gmail.com', 'phone': '123', 'date': 'invalid_date'}
        response = self.send_post_request(form_data)
        self.assertIn('{"name": "TYPE_TEXT", "email": "TYPE_EMAIL", "phone": "TYPE_TEXT", "date": "TYPE_TEXT"}', response)


if __name__ == '__main__':
    unittest.main(verbosity=2)
