import unittest
import arrayavg


class TestArrayAvg(unittest.TestCase):
    def test_arrayAvg1(self):
        result = arrayavg.getGreaterThanAvg([3, 2, 1])
        self.assertEqual(result, [3])
