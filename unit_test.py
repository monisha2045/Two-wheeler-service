import unittest
from unittest.mock import patch, MagicMock
from classes import *
from template import *


class TestTwo_wheel_service(unittest.TestCase):

    # @patch.object(Register, 'login', return_value=True)
    # def test_register_successful_login(self, mock_login):
    #     service = Two_wheel_service()
    #     result = service.register("test_user", "test_password")
    #     self.assertTrue(result)

    def test_create_customer(self):
        service = Two_wheel_service()
        customer = service.create_customer("John Doe", "123 Main St", "555-1234")
        self.assertIsInstance(customer, Customer)

    def test_create_order(self):
        service = Two_wheel_service()
        customer = MagicMock(spec=Customer)
        order = service.create_order(customer, "Motorcycle", "ABC123")
        self.assertIsInstance(order, Order)

    def test_add_service(self):
        service = Two_wheel_service()
        order = MagicMock(spec=Order)
        service.add_service(order, "puncture")
        order.add_service.assert_called_once()

    def test_finish(self):
        service = Two_wheel_service()
        order = MagicMock(spec=Order)
        service.finish(order)
        order.finish.assert_called_once()

    @patch.object(Mechanic, 'get_orders')
    def test_get_order(self, mock_get_orders):
        service = Two_wheel_service()
        mechanic = MagicMock(spec=Mechanic)
        service.get_order(mechanic)
        mechanic.get_orders.assert_called_once()

    @patch.object(Mechanic, 'update_status')
    def test_update(self, mock_update_status):
        service = Two_wheel_service()
        mechanic = MagicMock(spec=Mechanic)
        service.update(mechanic)
        mechanic.update_status.assert_called_once()


if __name__ == '__main__':
    unittest.main()