import unittest
import arrayavg


class testArrayavg(unittest.TestCase):
    def test_CalcAvg(self):
        result = arrayavg.CalcAvg([1, 2, 3])
        self.assertEqual(result, 2)

    def test_CalcAvg2(self):
        result = arrayavg.CalcAvg([-8, 0, 9])
        self.assertEqual(result, 0.3333333333333333)

    def test_CalcAvg3(self):
        result = arrayavg.CalcAvg([-81, 90, 129, 47, 25, 11, -8, 202])
        self.assertEqual(result, 51.875)
