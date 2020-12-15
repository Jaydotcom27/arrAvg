import unittest
import arrayavg


class testArrayavg(unittest.TestCase):
    def test_CalcAvg(self):
        result = arrayavg.CalcAvg([1, 2, 3])
        self.assertEqual(result, 2)

    def test_CalcAvg2(self):
        result = arrayavg.CalcAvg([-8, 0, 9])
        self.assertEqual(result, 0.3333333333333333)
