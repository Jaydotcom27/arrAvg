import unittest
import arrayavg


class TestArrayAvg(unittest.TestCase):
    def test_sum(self):
        result = arrayavg.CalcSum([1, 2, 3])
        self.assertEqual(result, 6)
