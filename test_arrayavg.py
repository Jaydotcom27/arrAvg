import unittest
import arrayavg


class testArrayavg(unittest.TestCase):
    def test_CalcAvg(self):
        result = arrayavg.CalcAvg([1, 2, 3])
        self.assertEqual(result, 2)
