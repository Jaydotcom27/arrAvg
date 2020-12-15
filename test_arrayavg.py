import unittest
import arrayavg


class TestArrayAvg(unittest.TestCase):
    def test_sum(self):
        result = arrayavg.CalcSum([1, 2, 3])
        self.assertEqual(result, 6)

    def test_sum2(self):
        result = arrayavg.CalcSum([-4, 4, 16])
        self.assertEqual(result, 16)

    def test_sum3(self):
        result = arrayavg.CalcSum([0, -2, 5, 3, 1])
        self.assertEqual(result, 7)

    def test_avg(self):
        result = arrayavg.CalcAvg([4, 7, 2], 13)
        self.assertEqual(result, 4.333333333333333)

    def test_avg2(self):
        result = arrayavg.CalcAvg([-2, 5, 6, 7], 16)
        self.assertEqual(result, 4)

    def test_avg3(self):
        result = arrayavg.CalcAvg([9, 8, 7, -11, 4, 25, 98],  140)
        self.assertEqual(result, 20)

    def test_greater(self):
        result = arrayavg.getGreater([4, 7, 2], 4.333333333333333)
        self.assertEqual(result, [7])
