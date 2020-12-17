import unittest
import arrayavg


class TestArrayAvg(unittest.TestCase):
    def test_arrayAvg1(self):
        result = arrayavg.getGreaterThanAvg([3, 2, 1])
        self.assertEqual(result, [3])

    def test_arrayAvg2(self):
        result = arrayavg.getGreaterThanAvg([13, 23, -51])
        self.assertEqual(result, [13, 23])

    def test_arrayAvg3(self):
        result = arrayavg.getGreaterThanAvg([13, 22, 31, 41, 53, 67, -8, 28])
        self.assertEqual(result, [31, 41, 53, 67])

    def test_arrayAvg4(self):
        result = arrayavg.getGreaterThanAvg([-5, 10, 5, 645])
        self.assertEqual(result, [645])

    def test_arrayAvg5(self):
        result = arrayavg.getGreaterThanAvg([8, 11, 12, 13, 14, 15, 268, -52])
        self.assertEqual(result, [268])
