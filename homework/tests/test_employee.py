import unittest
from unittest.mock import patch

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.empl = Employee('First', 'Test', 100)

    def test_return_first_name(self):
        self.assertEqual(self.empl.first, 'First')

    def test_return_last_name(self):
        self.assertEqual(self.empl.last, 'Test')

    def test_return_pay(self):
        self.assertEqual(self.empl.pay, 100)

    def test_set_last_name(self):
        self.empl.last = 'Last'
        self.assertEqual(self.empl.last, 'Last')

    def test_set_fist_name(self):
        self.empl.last = 'Test'
        self.assertEqual(self.empl.last, 'Test')

    def test_apply_raise(self):
        self.empl.apply_raise()
        self.assertEqual(self.empl.pay, 105)

    def test_email(self):
        self.assertEqual(self.empl.email, 'First.Test@email.com')

    def test_fullname(self):
        self.assertEqual(self.empl.fullname, 'First Test')

    @patch('requests.get')
    def test_monthly_schedule(self, mocker):
        class MyMock():
            ok = True
            text = 'First Test'

        mocker.return_value = MyMock()
        self.assertEqual(self.empl.monthly_schedule(10), 'First Test')
