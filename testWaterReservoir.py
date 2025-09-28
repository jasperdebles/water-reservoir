import unittest
from waterReservoir import WaterReservoir 

class TestWaterReservoir(unittest.TestCase):
    def setUp(self):
        # standard tank of 1000 liter with start level 0
        self.tank = WaterReservoir(max_level = 1000, min_level = 0, flow_rate = 50, level = 0)

    def test_initial_level(self):
        # test initial level of zero
        self.assertEqual(self.tank.get_level(), 0)

    def test_fill_within_limits(self):
        # test filling of tank within limits
        self.tank.fill(350)
        self.assertEqual(self.tank.get_level(), 350)

    def test_fill_overflow(self):
        # test filling of tank with overflow
        self.assertEqual(self.tank.fill(3000), 1000)
        self.assertEqual(self.tank.get_level(), 1000)

    def test_drain_within_limits(self):
        # test draining of tank within limits
        self.tank.fill(500)
        self.assertEqual(self.tank.drain(100), 100)
        self.assertEqual(self.tank.get_level(), 400)

    def test_drain_underflow(self):
        # test draining of tank with underflow
        self.tank.fill(500)
        self.assertEqual(self.tank.drain(800), 500)
        self.assertEqual(self.tank.get_level(), 0)

    def test_fill_invalid_amount(self):
        # test for input greater than zero
        with self.assertRaises(ValueError): 
            self.tank.fill(-10)

    def test_drain_invalid_amount(self):
        # test for input greater than zero
        with self.assertRaises(ValueError): 
            self.tank.drain(-10)

    def test_time_to_fill(self):
        # test time (minutes) to fill 
        self.assertEqual(self.tank.time_to_fill(500), 10)

    def test_time_to_drain(self):
        # test time (minutes) to drain
        self.tank.fill(500)
        self.assertEqual(self.tank.time_to_drain(200), 4)
